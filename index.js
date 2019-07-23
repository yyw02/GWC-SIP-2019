console.log("Hello World!");

var i = 0;
for (i = 0; i < 21; i+=2){
  console.log(i);
}

i = 0; // sets i to zero
while( i <= 20){  // runs when i <= 20
  if(i%2 == 0){
    console.log(i);
  }
  i += 1;
}


function getTemp(){
  return 22.5;
}
var temperature = getTemp();
console.log(temperature);

function getTemp2(type){
  if (type == "C"){
    alert("It is rainy today!");
    return 22.5;
  }
  if (type == "F"){
    alert("It is really hot today!");
    return 100;
  }
}
console.log(getTemp2("C"))
console.log(getTemp2("F"))
