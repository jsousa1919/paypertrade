urls = {
    base_index: "${ h.url_for(controller='base', action='index') }",
    base_signup: "${ h.url_for(controller='base', action='signup', secure=True) }",
    account_signin: "${ h.url_for(controller='account', action='signin', secure=True) }",
    account_authenticate: "${ h.url_for(controller='account', action='authenticate', secure=True) }",
    account_signout: "${ h.url_for(controller='account', action='signout') }",
    account_home: "${ h.url_for(controller='account', action='home', secure=True) }"
}
