"""SQLAlchemy Metadata and Session object"""
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer

__all__ = ['Base', 'Session']

# SQLAlchemy session manager. Updated by model.init_model()
Session = scoped_session(sessionmaker())

# The declarative Base

class Base(AbstractConcreteBase, declarative_base()):

    @classmethod
    def get(cls, id):
        return Session.query(cls).filter_by(id=id).one()

    @classmethod
    def find(cls, **kwargs):
        return Session.query(cls).filter_by(**kwargs).one()

    @classmethod
    def find_all(cls, **kwargs):
        return Session.query(cls).filter_by(**kwargs).all()
