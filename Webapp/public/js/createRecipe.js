componentHandler.upgradeDom();
var recipeList = [];

$('#show-action1').click(function () {
  var segNum = 1;
  var inList = false;
  
  showDialog({
    title: '<h4 class="mdl-dialog__title">Amount: <output id="recipeSliderOut"></output> mL</h4>',
    text: '<p style="width:300px"><h3><input class="mdl-slider mdl-js-slider" type="range" id="recipeSliderIn" min=0 max=100 value=0.0 step=0.1 oninput="recipeSliderOut.value=recipeSliderIn.value"/></h3></p>',
    positive: {
      title: 'Okay',
      onClick: function (e) {
        var sliderVal = document.getElementById("recipeSliderOut");
        var recipe = {
          segment: segNum,
          amount: sliderVal.value
        };
        
        for(var i=0; i<recipeList.length; i++){
          // check if segment already exists in recipeList
          if(recipeList[i].segment==segNum){
            recipeList[i].amount = sliderVal.value
            inList = true;
          }
        }
        
        if(!inList) {
          recipeList.push(recipe);
        }
        
        console.log(recipeList);
      }
    }
  });
});

$('#show-action2').click(function () {
  var segNum = 2;
  var inList = false;
  
  showDialog({
    title: '<h4 class="mdl-dialog__title">Amount: <output id="recipeSliderOut"></output> mL</h4>',
    text: '<p style="width:300px"><h3><input class="mdl-slider mdl-js-slider" type="range" id="recipeSliderIn" min=0 max=100 value=0.0 step=0.1 oninput="recipeSliderOut.value=recipeSliderIn.value"/></h3></p>',
    positive: {
      title: 'Okay',
      onClick: function (e) {
        var sliderVal = document.getElementById("recipeSliderOut");
        var recipe = {
          segment: segNum,
          amount: sliderVal.value
        };
        
        for(var i=0; i<recipeList.length; i++){
          // check if segment already exists in recipeList
          if(recipeList[i].segment==segNum){
            recipeList[i].amount = sliderVal.value
            inList = true;
          }
        }
        
        if(!inList) {
          recipeList.push(recipe);
        }
        
        console.log(recipeList);
      }
    }
  });
});

$('#show-action3').click(function () {
  var segNum = 3;
  var inList = false;
  
  showDialog({
    title: '<h4 class="mdl-dialog__title">Amount: <output id="recipeSliderOut"></output> mL</h4>',
    text: '<p style="width:300px"><h3><input class="mdl-slider mdl-js-slider" type="range" id="recipeSliderIn" min=0 max=100 value=0.0 step=0.1 oninput="recipeSliderOut.value=recipeSliderIn.value"/></h3></p>',
    positive: {
      title: 'Okay',
      onClick: function (e) {
        var sliderVal = document.getElementById("recipeSliderOut");
        var recipe = {
          segment: segNum,
          amount: sliderVal.value
        };
        
        for(var i=0; i<recipeList.length; i++){
          // check if segment already exists in recipeList
          if(recipeList[i].segment==segNum){
            recipeList[i].amount = sliderVal.value
            inList = true;
          }
        }
        
        if(!inList) {
          recipeList.push(recipe);
        }
        
        console.log(recipeList);
      }
    }
  });
});

$('#show-action4').click(function () {
  var segNum = 4;
  var inList = false;
  
  showDialog({
    title: '<h4 class="mdl-dialog__title">Amount: <output id="recipeSliderOut"></output> mL</h4>',
    text: '<p style="width:300px"><h3><input class="mdl-slider mdl-js-slider" type="range" id="recipeSliderIn" min=0 max=100 value=0.0 step=0.1 oninput="recipeSliderOut.value=recipeSliderIn.value"/></h3></p>',
    positive: {
      title: 'Okay',
      onClick: function (e) {
        var sliderVal = document.getElementById("recipeSliderOut");
        var recipe = {
          segment: segNum,
          amount: sliderVal.value
        };
        
        for(var i=0; i<recipeList.length; i++){
          // check if segment already exists in recipeList
          if(recipeList[i].segment==segNum){
            recipeList[i].amount = sliderVal.value
            inList = true;
          }
        }
        
        if(!inList) {
          recipeList.push(recipe);
        }
        
        console.log(recipeList);
      }
    }
  });
});

$('#show-action5').click(function () {
  var segNum = 5;
  var inList = false;
  
  showDialog({
    title: '<h4 class="mdl-dialog__title">Amount: <output id="recipeSliderOut"></output> mL</h4>',
    text: '<p style="width:300px"><h3><input class="mdl-slider mdl-js-slider" type="range" id="recipeSliderIn" min=0 max=100 value=0.0 step=0.1 oninput="recipeSliderOut.value=recipeSliderIn.value"/></h3></p>',
    positive: {
      title: 'Okay',
      onClick: function (e) {
        var sliderVal = document.getElementById("recipeSliderOut");
        var recipe = {
          segment: segNum,
          amount: sliderVal.value
        };
        
        for(var i=0; i<recipeList.length; i++){
          // check if segment already exists in recipeList
          if(recipeList[i].segment==segNum){
            recipeList[i].amount = sliderVal.value
            inList = true;
          }
        }
        
        if(!inList) {
          recipeList.push(recipe);
        }
        
        console.log(recipeList);
      }
    }
  });
});

$('#show-action6').click(function () {
  var segNum = 6;
  var inList = false;
  
  showDialog({
    title: '<h4 class="mdl-dialog__title">Amount: <output id="recipeSliderOut"></output> mL</h4>',
    text: '<p style="width:300px"><h3><input class="mdl-slider mdl-js-slider" type="range" id="recipeSliderIn" min=0 max=100 value=0.0 step=0.1 oninput="recipeSliderOut.value=recipeSliderIn.value"/></h3></p>',
    positive: {
      title: 'Okay',
      onClick: function (e) {
        var sliderVal = document.getElementById("recipeSliderOut");
        var recipe = {
          segment: segNum,
          amount: sliderVal.value
        };
        
        for(var i=0; i<recipeList.length; i++){
          // check if segment already exists in recipeList
          if(recipeList[i].segment==segNum){
            recipeList[i].amount = sliderVal.value
            inList = true;
          }
        }
        
        if(!inList) {
          recipeList.push(recipe);
        }
        
        console.log(recipeList);
      }
    }
  });
});

$('#show-action7').click(function () {
  var segNum = 7;
  var inList = false;
  
  showDialog({
    title: '<h4 class="mdl-dialog__title">Amount: <output id="recipeSliderOut"></output> mL</h4>',
    text: '<p style="width:300px"><h3><input class="mdl-slider mdl-js-slider" type="range" id="recipeSliderIn" min=0 max=100 value=0.0 step=0.1 oninput="recipeSliderOut.value=recipeSliderIn.value"/></h3></p>',
    positive: {
      title: 'Okay',
      onClick: function (e) {
        var sliderVal = document.getElementById("recipeSliderOut");
        var recipe = {
          segment: segNum,
          amount: sliderVal.value
        };
        
        for(var i=0; i<recipeList.length; i++){
          // check if segment already exists in recipeList
          if(recipeList[i].segment==segNum){
            recipeList[i].amount = sliderVal.value
            inList = true;
          }
        }
        
        if(!inList) {
          recipeList.push(recipe);
        }
        
        console.log(recipeList);
      }
    }
  });
});

$('#show-action8').click(function () {
  var segNum = 8;
  var inList = false;
  
  showDialog({
    title: '<h4 class="mdl-dialog__title">Amount: <output id="recipeSliderOut"></output> mL</h4>',
    text: '<p style="width:300px"><h3><input class="mdl-slider mdl-js-slider" type="range" id="recipeSliderIn" min=0 max=100 value=0.0 step=0.1 oninput="recipeSliderOut.value=recipeSliderIn.value"/></h3></p>',
    positive: {
      title: 'Okay',
      onClick: function (e) {
        var sliderVal = document.getElementById("recipeSliderOut");
        var recipe = {
          segment: segNum,
          amount: sliderVal.value
        };
        
        for(var i=0; i<recipeList.length; i++){
          // check if segment already exists in recipeList
          if(recipeList[i].segment==segNum){
            recipeList[i].amount = sliderVal.value
            inList = true;
          }
        }
        
        if(!inList) {
          recipeList.push(recipe);
        }
        
        console.log(recipeList);
      }
    }
  });
});
