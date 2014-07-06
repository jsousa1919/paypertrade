import logging
import random
import scrypt
import string

from sqlalchemy.schema import *
from sqlalchemy.types import *

from paypertrade.model.meta import Session, Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    password_seed = Column(String(64), nullable=False)
    email = Column(String(64))
    name = Column(String(64))

    @classmethod
    def create(cls, username, password):
        user = cls()
        user.username = username
        user.password_seed = ''.join(random.sample(string.printable, 64))
        user.password = scrypt.encrypt(password, user.password_seed, maxtime=2)
        Session.add(user)
        Session.commit()
        return user

