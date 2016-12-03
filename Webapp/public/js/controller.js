var app = angular.module('MyxApp', ['ngRoute','ngMaterial','ngMessages', 'material.svgAssetsCache'])
    .service("recipeServ", function() { 
        var _data = {}

        return {
            getData: function (){
                return _data;
            },
            setData: function (d) {
                _data = d;
            }
        }
    });

app.config(function($routeProvider, $locationProvider) {
    $routeProvider
    .when("/", {
        redirectTo: '/homepage',
        controller: 'MainCtrl'
    })
    .when("/editpage", {
        templateUrl: 'html/createRecipe.html',
        controller: 'EditCtrl'
    })
    .when("/homepage", {
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

app.controller("MainCtrl", function($scope, $route, $routeParams, $location, $http) {
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;

    $scope.clearSearch = function () {
        $scope.searchText= "";
                    
    };
});


app.controller("HomeCtrl", function($scope, recipeServ, $route, $routeParams, $location, $http, $mdDialog) {
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
    
    $scope.customFullscreen = false;
    
    $scope.removeRecipe = function(recipe) {
        $http.put("/homepage/remove", {recipe: recipe}).then(function() {
            getRecipes();
        });

    };
    
    $scope.editRecipe = function(d) { 
        recipeServ.setData(d);
    }

    $scope.sendRecipe = function (ev,data) {
        var recipe = data.contents.recipe;
        var recipeCSV = "";

        $mdDialog.show(
            $mdDialog.alert()
            .parent(angular.element(document.getElementsByClassName(".mdl-layout__container")))
            .clickOutsideToClose(true)
            .title('Recipe Sent...')
            .textContent('Sit tight, in a couple moments your drink will be served!')
            .ariaLabel('Alert Dialog Demo')
            .ok('Got it!')
            .targetEvent(ev)
        );

        for (var i=0; i<recipe.ingredients.length; i++) {
            recipeCSV = recipeCSV.concat(recipe.ingredients[i].segment.toString()
                + "," + recipe.ingredients[i].amount.toString() + ",");
        
        }

        if (recipe.ordered == "Is Ordered") {
            recipeCSV = recipeCSV.concat("true");
        } else {
            recipeCSV = recipeCSV.concat("false");
        }

        $http.put("/myxrecipe",{data: recipeCSV}).then(function () {
            getRecipes();
        });
    }

    function getRecipes() {
        $http.get('/homepage').then(function (response) {
            $scope.recipes = response.data;
        });
    }

    getRecipes();
   
});

app.controller("EditCtrl", function($scope, recipeServ, $route, $routeParams, $location, $http, $mdDialog) {
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
    $scope.customFullscreen = false;

    $scope.recipe = {
        name: "",
        ordered: "Not Ordered",
        ingredients: [],
        author: "",
        time: 0
    }

    $scope.recipe  = recipeServ.getData().contents.recipe;
    //----------------------------------------------//

    $scope.deleteIngredient = function (index) {
        $scope.recipe.ingredients.splice(index,1);
    };
    
    $scope.submitNewRecipe = function() {
        $http.put("/editpage", {recipe: $scope.recipe}).then(function() {
            $scope.recipe.name = "";
        });
        
    };
    
    $scope.showRecipeAmt = function(event, seg) {
        var inList = false;
        
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
            var ingredient = {
                segment: seg,
                amount: amt
            }
            
            for(var i=0; i<$scope.recipe.ingredients.length; i++) {
                if($scope.recipe.ingredients[i].segment == seg) {
                    $scope.recipe.ingredients[i].amount = amt;
                    inList = true;
                }
            }
            
            if(!inList) {
                $scope.recipe.ingredients.push(ingredient);
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

app.controller("RecipeCtrl", function($scope, $route, $routeParams, $location, $http, $mdDialog) {
    
    // ngRoute settings
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
    
    // mdDialog settings
    $scope.customFullscreen = false;
    
    $scope.recipe = {
        name: "",
        ordered: "Not Ordered",
        ingredients: [],
        author: "",
        time: 0
    }
    
    $scope.deleteIngredient = function (index) {
        $scope.recipe.ingredients.splice(index,1);
    };
    
    $scope.submitNewRecipe = function() {
        $scope.recipe.time = (new Date).getTime();
        
        $http.post("/homepage", {recipe: $scope.recipe}).then(function() {
            $scope.recipe.name = "";
            
        });
        
    };
    
    $scope.showRecipeAmt = function(event, seg) {
        var inList = false;
        
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
            var ingredient = {
                segment: seg,
                amount: amt
            }
            
            for(var i=0; i<$scope.recipe.ingredients.length; i++) {
                if($scope.recipe.ingredients[i].segment == seg) {
                    $scope.recipe.ingredients[i].amount = amt;
                    inList = true;
                }
            }
            
            if(!inList) {
                $scope.recipe.ingredients.push(ingredient);
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
