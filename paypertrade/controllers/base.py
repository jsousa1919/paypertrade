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
        return render_mako('index.mako')

    def template_error(self):
        c.users = model.Session.query(model.User).all()
        return render_mako('error.mako')

    def error(self):
        c.users = model.Session.query(model.DoesntExist).all()
        return render_mako('error.mako')
