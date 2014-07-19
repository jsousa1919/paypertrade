%if h.user():
    you are signed in why are you here?
%endif

<form method="post" action="${ h.url_for(controller='account', action='authenticate') }">
    <div>
        <input name="email" placeholder="Email" />
    </div>
    <div>
        <input name="password" placeholder="Password" />
    </div>
    <div>
        <label>Remember Me</label>
        <input type="checkbox" name="remember" />
    </div>
    <div>
        <input type="submit" value="Submit" />
    </div>
</form>
<a href="https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=${ config.get('google_client_id') }&redirect_uri=${ h.url_for(controller='account', action='google_callback', secure=True) }&scope=profile email">Sign in with Google</a>
