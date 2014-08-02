<%inherit file="../base/html.mako" />
<%def name="title()">Signin</%def>
<%def name="head()"></%def>
<%def name="ready()"></%def>

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
<span id="signinButton">
    <span
    class="g-signin"
    data-callback="authenticate"
    data-clientid="${ config.get('google_client_id') }"
    data-cookiepolicy="single_host_origin"
    data-scope="https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/books">
    </span>
</span>
