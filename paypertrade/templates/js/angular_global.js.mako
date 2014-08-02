$.PayPerTrade = angular.module('PayPerTrade', []);

$.PayPerTrade.service('GlobalService', function($rootScope) {});

$.PayPerTrade.controller('GlobalCtrl', function($scope, GlobalService) {
    $scope.urls = urls;
});
