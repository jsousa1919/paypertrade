Sign up on paypertrade
<div>
    <form href="${ h.url_for(controller='account', action='signup') }" method="POST">
        <input name="email" placeholder="Email"></input>
        <br />
        <input name="password" placeholder="Password"></input>
        <input type="submit" value="Sign up"></input>
    </form>
</div>
<div>
    Or sign up with your google account
    <a href="https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=${ config.get('google_client_id') }&redirect_uri=${ h.url_for(controller='account', action='signup_google', secure=True) }&scope=profile email">Sign in with Google</a>
