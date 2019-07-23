var adj = ["brave", "resilient", "lovely", "happy", "lvely","friendly", "kind"];
var pos = 0;
var loc = document.getElementById("abc");

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos =0;
    }
  }

var x = document.getElementsByTagName("body")[0]
function colorfulBackground(){
  x.setAttribute("style", `background-color:rgb(${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)})`)
}
