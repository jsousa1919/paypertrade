function google_authenticate(authResult) {
    if (authResult['status']['signed_in']) {
        $.GlobalCtrl.google_login(authResult);
        gapi.client.load('oauth2', 'v2', function() {
            gapi.client.oauth2.userinfo.get().execute(function(resp) {
                $.GlobalCtrl.$broadcast('google_signin', resp);
            })
        });
    } else {
        console.log('Sign-in state: ' + authResult['error']);
    }
};
