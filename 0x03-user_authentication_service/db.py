#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from user import User
from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession: sessionmaker[Session] = sessionmaker(bind=self._engine)
            self.__session = DBSession()  # type: ignore
        return self.__session  # type: ignore

    def add_user(self, email: str, hashed_password: str) -> User:
        """adds user to the database a.db"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """finds data by positional arguments"""
        if not kwargs:
            raise InvalidRequestError()

        query = self._session.query(User)
        result: User | None = query.filter_by(**kwargs).first()

        if result is None:
            raise NoResultFound()
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        updates user data if of a given id with
        the kwargs as the key value pair
        """
        findUser = self.find_user_by(id=user_id)
        if not findUser:
            raise ValueError()

        for key, value in kwargs.items():
            if hasattr(findUser, key):
                setattr(findUser, key, value)
            else:
                raise AttributeError()

        self._session.commit()
        return None
