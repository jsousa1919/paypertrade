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
        password = self.data('password')
        remember = self.data('remember')

        user = model.User.find(email=email)

        #TODO differentiate between post and json requests
        # best to add a helper in global use in this case
        if user and user.authenticate(password):
            h.save_user(user.id, remember=remember)
            h.redirect_to(controller='account', action='home')
        else:
            h.redirect_to(controller='base', action='index')

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

    def signup(self):
        return render('account/signup.mako')
