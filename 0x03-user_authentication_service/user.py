#!/usr/bin/env python3
"""CREATE A USER CLASS FOR AUTENTICATION"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from typing import Any

Base: Any = declarative_base()


class User(Base):
    """User data the creates the users in a database
    with an id, email address and session id it also
    creates the user password
    """

    __tablename__: str = 'users'

    id: Column[int] = Column(Integer, primary_key=True)
    email: Column[str] = Column(String(250), nullable=False)
    hashed_password: Column[str] = Column(String(250), nullable=False)
    session_id: Column[str] = Column(String(250), nullable=True)
    reset_token: Column[str] = Column(String(250), nullable=True)
