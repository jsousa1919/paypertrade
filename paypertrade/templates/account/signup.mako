<%inherit file="../base/html.mako" />
<%def name="title()">Welcome to PayPerBook, we love you</%def>
<%def name="head()">
    <script>
        $.PayPerTrade.controller('SignupCtrl', function($scope, $http) {
            $scope.submit = function () {
                $http.post(urls.base_signup, {
                    email: $scope.email,
                    password: $scope.password,
                    google_id: $scope.google_id,
                    google_token: $scope.google_token,
                    name: $scope.name
                })
                .success(function(resp) {
                    alert('Signed Up!');
                })
                .error(function(resp) {
                    alert(resp);
                });
            };
            $scope.$on('google_signin', function(event, resp) {
                $scope.email = resp.email;
                $scope.name = resp.given_name;
                $scope.google_id = resp.id;
                $scope.submit();
            });
        });
    </script>
</%def>

Sign up on paypertrade
<div>
    <form ng-controller="SignupCtrl">
        <input name="email" ng-model="email" placeholder="Email"></input>
        <br />
        <input name="password" ng-model="password" placeholder="Password"></input>
        <input type="submit" ng-click="submit()" value="Sign up"></input>
    </form>
</div>
<div>
    <div>
        Or sign up with one of these!
    </div>
    <span id="signinButton">
        <span
        class="g-signin"
        data-callback="google_authenticate"
        data-clientid="${ config.get('google_client_id') }"
        data-cookiepolicy="single_host_origin"
        data-scope="https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/books">
        </span>
    </span>
</div>
