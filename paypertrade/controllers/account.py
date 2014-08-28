import simplejson
from paypertrade.lib.base import *

class AccountController(BaseCtrl):
    def signin(self):
        if h.user():
            h.redirect_to(controller='account', action='home')
        else:
            return render('/account/signin.mako')

    def signout(self):
        h.clear_user()
        h.redirect_to(controller='base', action='index')

    #TODO https
    def authenticate(self):
        email = self.data('email')
        user = model.User.find(email=email)

        if user:
            remember = self.data('remember')
            google_token = self.data('google_token')
            password = self.data('password')

            if user.authenticate(password=password, google_token=google_token):
                h.save_user(user.id, remember=remember)
                return simplejson.dumps({'status': 'success'})

        return simplejson.dumps({'status': 'error'})

    def home(self):
        if h.user():
            return render('/account/home.mako')
        else:
            h.redirect_to(controller='account', action='signin')

    def google_callback(self):
        error = request.params.get('error')
        if error:
            return error

        code = request.params.get('code')
        return code
