#!/usr/bin/env python3
"""
Route module for the API
"""
from typing import Tuple
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
AUTH_TYPE = os.getenv("AUTH_TYPE")

try:
    if AUTH_TYPE == 'auth':
        from api.v1.auth.auth import Auth
        auth = Auth()
    elif AUTH_TYPE == 'basic_auth':
        from api.v1.auth.basic_auth import BasicAuth
        basic_auth = BasicAuth()
except ImportError as e:
    print("Error importing Auth class:", e)

@app.errorhandler(404)
def not_found(error) -> Tuple[str, int]:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error):
    """unauthorized acces"""
    response = jsonify({"error": "Unauthorized"})
    return response, 401 

@app.errorhandler(403)
def forbidden(error):
    """forbidden link"""
    response = jsonify({"error": "Forbidden"})
    return response, 403

@app.before_request
def handles_requests():
    """handels requests"""
    try:
        if auth is None:
            return

        path_list = ['/api/v1/status/',
                     '/api/v1/unauthorized/', '/api/v1/forbidden/']

        if request.path not in path_list:
            auth.require_auth(request.path, excluded_paths=path_list)

        auth_header = auth.authorization_header(request)
        print("Authorization header in handles_requests:", auth_header)
        if auth_header is None:
            abort(401, description="Unauthorized")

        # Check for current user
        current_user = auth.current_user(request)
        print("Current user in handles_requests:", current_user)
        if current_user is None:
            abort(403, description="Forbidden")
    except Exception as e:
        print("Error in before_request_handler:", e)
        abort(500)

if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
