import logging

from pylons import config, tmpl_context as c
from pylons.templating import render_mako
import sqlalchemy as sa

from paypertrade import model
from paypertrade.lib.base import *


log = logging.getLogger(__name__)

class BaseController(BaseController):
    def index(self):
        c.users = model.Session.query(model.User).all()
        fake1 = object()
        fake1.name = 'I do have objects'
        fake1.email = 'just a list of objects'
        fake1.username = 'all the same'
        c.fakes = [fake1]
        return render_mako('index.mako')

    def template_error(self):
        c.users = model.Session.query(model.User).all()
        return render_mako('error.mako')

    def error(self):
        c.users = model.Session.query(model.DoesntExist).all()
        return render_mako('error.mako')
