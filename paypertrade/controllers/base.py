from paypertrade.lib.base import *

log = logging.getLogger(__name__)


class BaseController(BaseCtrl):
    def index(self):
        c.users = model.Session.query(model.User).all()
        if h.user():
            c.status = 'AUTHENTICATED!'
        else:
            c.status = 'BE GONE HOODLUM!'
        return render('base/index.mako')

    def signup(self):
        email = self.data('email')
        if email:
            password = self.data('password')

            google_id = self.data('google_id')
            if google_id:
                google_token = self.data('google_token')
                name = self.data('name')
                user = model.User.create_google(email, google_id, google_token, name=name)
            else:
                user = model.User.create(email, password)
            h.save_user(user.id)
            h.redirect_to(controller='account', action='home')

        return render('account/signup.mako')

    def template_error(self):
        c.users = model.Session.query(model.User).all()
        return render('error.mako')

    def error(self):
        c.users = model.Session.query(model.DoesntExist).all()
        return render('error.mako')
