#!/usr/bin/env python3
"""authentication of user data"""
from flask import request
from typing import List, TypeVar, Union


class Auth:
    """enables authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """required authentication"""
        if path is None:
            return True

        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> Union[str, None]:
        """header autorization"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """checks current user"""
        return None
