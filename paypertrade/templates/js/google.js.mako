function authenticate(authResult) {
    if (authResult['status']['signed_in']) {
        gapi.client.load('oauth2', 'v2', function() {
            gapi.client.oauth2.userinfo.get().execute(function(resp) {
                console.log(resp.email);
            })
        });
    } else {
        console.log('Sign-in state: ' + authResult['error']);
    }
};
