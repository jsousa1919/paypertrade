import hashlib

from pylons import config, request, response, session, tmpl_context as c, url
from pylons.controllers import WSGIController
from pylons.controllers.util import redirect
from pylons.templating import render_mako as render
import sqlalchemy as sqa

from paypertrade import model

COOKIE_SALT = "WE'RE SAILORS ON THE MOON, WE CARRY A HARPOON!"

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            model.Session.remove()

    def data(key, default):
        try:
            return request.params.get(key) or request.json.get(key)
        except KeyError:
            return None

