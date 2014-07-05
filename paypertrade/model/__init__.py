import logging

from paypertrade.model.meta import Session, Base
from paypertrade.model.core import *

log = logging.getLogger(__name__)

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
