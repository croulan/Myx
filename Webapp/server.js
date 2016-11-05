
var express = require("express");
var MongoClient = require("mongodb").MongoClient;
var ObjectId = require('mongodb').ObjectID;
var bodyparse = require("body-parser");
var app = express();

var db = null;

app.use(bodyparse.json());
app.use(express.static('public'));
app.use(express.static('node_modules'));

MongoClient.connect('mongodb://localhost:27017/mittens', function(err, dbconn) {
    if (!err) {
        console.log('Connection Successful');
        db = dbconn;
    }
});

app.get('/homepage', function (req, res, next) {
    db.collection('meows', function(err, recipeCollection) {
        recipeCollection.find().toArray(function(err, recipes) {
            return res.json(recipes);

        });

    });

});

app.put('/homepage/remove', function(req,res,next) {
    db.collection('meows', function(err, recipeCollection){
        var recipeId = req.body.recipe._id;
        recipeCollection.remove({_id: ObjectId(recipeId)}, {w:1}, function(err, result) {
            return res.send();

        });
    });

});

app.post('/homepage', function (req, res, next) {
    
    db.collection('meows', function(err, recipeCollection) {
        var newRecipe = { text: req.body.newRecipe };
        
        recipeCollection.insert(newRecipe, {w:1}, function(err) {
            return res.send();

        });

    });

});

app.listen(3000, function () {
    console.log("Listening on port 3000");
});
