urls = {
    base_index: "${ h.url_for(controller='base', action='index') }",
    base_signup: "${ h.url_for(controller='base', action='signup') }",
    account_signin: "${ h.url_for(controller='account', action='signin') }",
    account_signout: "${ h.url_for(controller='account', action='signout') }",
    account_home: "${ h.url_for(controller='account', action='home') }"
}
