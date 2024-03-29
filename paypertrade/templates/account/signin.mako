<%inherit file="../base/html.mako" />
<%def name="title()">Signin</%def>
<%def name="head()"></%def>
<%def name="ready()"></%def>

%if h.user():
    you are signed in why are you here?
%endif

<login-form></login-form>
<span id="signinButton">
    <span
    class="g-signin"
    data-callback="google_authenticate"
    data-clientid="${ config.get('google_client_id') }"
    data-cookiepolicy="single_host_origin"
    data-scope="https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/books">
    </span>
</span>

<%def name="post()">
    %if not h.user():
        <script type="text/javascript">
            (function() {
                var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                po.src = 'https://apis.google.com/js/client:plusone.js';
                    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
                }
            )();
        </script>
    %endif
</%def>
