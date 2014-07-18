from paypertrade.lib.base import *

log = logging.getLogger(__name__)


class BaseController(BaseCtrl):
    def index(self):
        c.users = model.Session.query(model.User).all()
        if h.user():
            c.status = 'AUTHENTICATED!'
        else:
            'BE GONE HOODLUM!'
        return render('index.mako')

    def template_error(self):
        c.users = model.Session.query(model.User).all()
        return render('error.mako')

    def error(self):
        c.users = model.Session.query(model.DoesntExist).all()
        return render('error.mako')
