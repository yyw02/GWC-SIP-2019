console.log("Hello World");

var h1tag = document.getElementsByTagName('h1')[0];
var pos = 0;
var loc = document.getElementsByClassName("headings")[3];

var adi = ["brave", "resilient", "lovely", "happy"]

document.getElementById("adj")

function changAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos =0;
    }
  }
