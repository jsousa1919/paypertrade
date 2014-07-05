import logging

from sqlalchemy.schema import *
from sqlalchemy.types import *

from paypertrade.model.meta import Session, Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(64))
    name = Column(String(64), nullable=False)
