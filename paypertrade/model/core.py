import bcrypt
import logging
import random
import string

from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import String, Integer

from paypertrade.lib.helpers import superhelpers as sh
from paypertrade.model.meta import Session, Base

class User(Base):
    SCRYPT_PARAMS = {
        'N': 1 << 16,
        'r': 16,
        'p': 2
    }
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True)
    password = Column(String(256))
    google_id = Column(String(256))
    google_token = Column(String(256))
    name = Column(String(64))

    @classmethod
    def create(cls, email, password, **kwargs):
        user = cls()
        user.email = email
        user.password = bcrypt.hashpw(password, bcrypt.gensalt())
        user.__dict__.update(kwargs)
        Session.add(user)
        Session.commit()
        return user

    @classmethod
    def create_google(cls, email, uid, token, **kwargs):
        user = cls()
        user.email = email
        user.googe_id = uid
        user.google_token = token
        user.__dict__.update(kwargs)
        Session.add(user)
        Session.commit()
        return user

    def authenticate(self, password=None, google_token=None):
        if google_token:
            # TODO best practices on secure, reversible, token storage
            # TODO token refresh
            return user.google_token == google_token
        else:
            return bcrypt.checkpw(password or '', self.password)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    isbn = Column(String(32), unique=True, nullable=False)
    authors = relationship('BookAuthorMap', backref='book')
    tags = relationship('BookTagMap', backref='book')

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

class BookAuthorMap(Base):
    __tablename__ = 'book_author_map'
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)
    author = relationship('Author', backref='books')

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

class BookTagMap(Base):
    __tablename__ = 'book_tag_map'
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)
    tag = relationship('Tag', backref='books')


