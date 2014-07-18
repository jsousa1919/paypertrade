%if h.user():
    you are signed in why are you here?
%endif

<form method="post" action="${ h.url(controller='account', action='authenticate') }">
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
