
var app = angular.module('mittens', []);

app.controller("MyxCtrl", function($scope, $http) {

    $scope.submitNewMeow = function() {
        $http.post("/homepage", {newMeow: $scope.newMeow}).then(function() {
            getMeows();
            $scope.newMeow = "";
        });
    };
    
    $scope.removeMeow = function(meow) {
        $http.put("/homepage/remove", {meow: meow}).then(function() {
            getMeows();
        });
    };

    function getMeows() {
        $http.get('/homepage').then(function (response) {
            $scope.meows = response.data;
        });
    };

    getMeows();

});
