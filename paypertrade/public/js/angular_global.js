$.PayPerTrade = angular.module('PayPerTrade', []);

$.PayPerTrade.service('GlobalService', function($rootScope) {});

$.PayPerTrade.controller('GlobalCtrl', function($scope, GlobalService) {
    $.GlobalCtrl = $scope;
    $scope.urls = urls;

    $scope.google_login = function(authResult) {
        $scope.google_token = authResult.access_token;
    };
});

$.PayPerTrade.directive('loginForm', function ($rootScope, $http) {
    return {
        restrict: 'E',
        templateUrl: '/partials/signin.html',
        scope: {
            email: '@'
        },
        link: function($scope, element, attrs) {
            
        },
        controller: function($scope) {
            $scope.submit = function () {
                $http.post(urls.account_authenticate, {
                    email: $scope.email,
                    password: $scope.password,
                    remember: $scope.remember,
                    google_token: $.GlobalCtrl.google_token,
                    fb_token: $.GlobalCtrl.fb_token
                })
                .success(function(resp) {
                    window.open($.GlobalCtrl.urls.account_home, '_self');
                })
                .error(function(resp) {
                    alert(resp);
                });
            };
            $scope.$on('google_signin', function(event, resp) {
                $scope.email = resp.email;
                $scope.submit();
            });
        }
    }
});
