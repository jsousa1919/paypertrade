import hashlib
import logging
from simplejson import JSONDecodeError

from pylons import config, request, response, session, tmpl_context as c, url
from pylons.controllers import WSGIController
from pylons.controllers.util import redirect
from pylons.templating import render_mako as render
import sqlalchemy as sqa

from paypertrade import model
from paypertrade.lib import helpers as h


class BaseCtrl(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            model.Session.remove()

    def data(self, key, default=None):
        try:
            return request.params.get(key) or request.json.get(key)
        except (KeyError, JSONDecodeError) as e:
            return None

