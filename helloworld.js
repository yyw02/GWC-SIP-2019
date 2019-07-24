var adj = ["brave", "resilient", "lovely", "happy", "lvely","friendly", "kind"];
var pos = 0;
var loc = document.getElementById("abcdefghij");

// function changeAdj(){
//   loc.innerHTML = adjectives[pos];
//   pos ++;
//   if (pos >= adjectives.length){
//     pos = 0;
//     }
//   }

var x = document.getElementById("colorChange")
function colorfulBackground(){
  x.setAttribute("style", `background-color:rgb(${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)})`)
}

  var foz = document.getElementById("the name")
 function changeFontColor(){
   foz.setAttribute("style", "color:blue");
 }



var font = ["'Bonbon', cursive;","'Butcherman', cursive;", "'Fascinate', cursive;", "'Indie Flower', cursive;", "'Lobster', cursive;", "'Abel', sans-serif;"];
var poz = 0;
function fontChange(){
  foz.setAttribute("style",)
}
