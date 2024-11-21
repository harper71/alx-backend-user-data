#!/usr/bin/env python3
"""handles the authentication of user"""
from db import DB
import bcrypt


def _hash_password(password: str) -> bytes:
    """this functions hashes the users password"""
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password



class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
    