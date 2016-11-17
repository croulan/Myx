var app = angular.module('MyxApp', ['ngRoute','ngMaterial','ngMessages', 'material.svgAssetsCache']);

app.config(function($routeProvider, $locationProvider) {
    $routeProvider
    .when("/", {
        templateUrl: 'html/homepage.html',
        controller: 'HomeCtrl'
    })
    .when("/createpage", {
        templateUrl: 'html/createRecipe.html',
        controller: 'RecipeCtrl'
    })
    .otherwise({
        redirectTo: '/'
    });
                    
});

app.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('blue-grey')
    .accentPalette('orange');
});

app.controller("HomeCtrl", function($scope, $route, $routeParams, $location, $http) {
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
    
    $scope.removeRecipe = function(recipe) {
        $http.put("/homepage/remove", {recipe: recipe}).then(function() {
            getRecipes();
        });

    };

    function getRecipes() {
        $http.get('/homepage').then(function (response) {
            $scope.recipes = response.data;
        });
    }

    getRecipes();
   
});

app.controller("RecipeCtrl", function($scope, $route, $routeParams, $location, $http, $mdDialog) {
    
    // ngRoute settings
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
    
    // mdDialog settings
    $scope.customFullscreen = false;
    
    $scope.recipeList= [];

    
    $scope.deleteIngredient = function (index) {
        $scope.recipeList.splice(index,1);
    };
    
    $scope.submitNewRecipe = function() {
        $http.post("/homepage", {newRecipe: $scope.newRecipe}).then(function() {
            $scope.newRecipe = "";
            
        });

    };
    
    $scope.showRecipeAmt = function(event, seg) {
        
        $mdDialog.show({
            controller:DialogController,
            templateUrl: "recipeSlider.html",
            parent: angular.element(document.getElementsByClassName(".mdl-layout__container")).scope(),
            targetEvent: event,
            clickOutsideToClose: true,
            title: "Amount in mL",
            ok: "Okay",
            fullscreen: $scope.customFullscreen
        })
        .then(function(amt) {
            var inList = false;
            var ingredient = {
                segment: seg,
                amount: amt
            }
            
            for(var i=0; i<$scope.recipeList.length; i++) {
                if($scope.recipeList.segment == seg) {
                    $scope.recipeList[i].amount = amt;
                    inList = true;
                }
            }
            
            if(!inList) {
                $scope.recipeList.push(ingredient);
                console.log($scope.recipeList);
            }
            
        });
    }
      
    function DialogController($scope, $mdDialog) {
        $scope.hide = function() {
            $mdDialog.hide();
        };
        
        $scope.cancel = function() {
            $mdDialog.cancel();
        };
        
        $scope.answer = function(answer) {
            $mdDialog.hide(answer);
        };
  }

});