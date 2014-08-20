$.PayPerTrade = angular.module('PayPerTrade', []);

$.PayPerTrade.service('GlobalService', function($rootScope) {});

$.PayPerTrade.controller('GlobalCtrl', function($scope, GlobalService) {
    $scope.urls = urls;
    $.GlobalCtrl = $scope;

    $scope.google_login = function(authResult) {
        $scope.google_token = authResult.access_token;
    };
});

$.PayPerTrade.directive('loginForm', function ($http) {
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
                $http.post(urls.authenticate, {
                    email: $scope.email,
                    password: $scope.password,
                    remember: $scope.remember,
                    google_code: $scope.google_code,
                    fb_code: $scope.fb_code
                })
                .success(function(resp) {
                    alert('yay');
                })
                .error(function(resp) {
                    alert(resp);
                });
            };
        }
    }
});
