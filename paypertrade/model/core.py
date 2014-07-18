import bcrypt
import logging
import random
import string

from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import String, Integer

from paypertrade.model.meta import Session, Base

class User(Base):
    SCRYPT_PARAMS = {
        'N': 1 << 16,
        'r': 16,
        'p': 2
    }
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(64))
    password = Column(String(256), nullable=False)
    token = Column(String(64))
    name = Column(String(64))

    @classmethod
    def create(cls, email, password):
        user = cls()
        user.email = email
        user.password = bcrypt.hashpw(password, user.password_salt)
        Session.add(user)
        Session.commit()
        return user

    def authenticate(self, password):
        return bcrypt.checkpw(password, user.password)


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


