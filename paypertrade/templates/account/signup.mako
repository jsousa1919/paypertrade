<%inherit file="../base/html.mako" />

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
</div>
