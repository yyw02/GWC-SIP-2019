
var pos = 0;
var loc = document.getElementsById("abc")

var adj = ["brave", "resilient", "lovely", "happy"]

document.getElementById("adj")

function changAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos =0;
    }
  }

Math.random()
var x = document.getElementsByTagName("body")[0]

function colorfulBackground(){
  x.setAttribute("style", `background-color:rgb(${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)})`)
}
