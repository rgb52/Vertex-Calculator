
var record = [];
///var fs = require('fs');

$(document).ready(function(){
var newRecords = "";


function aj() {
$.ajax({

url: "/Users/robberbee/Documents/GitHub/Vertex-Calculator/scrapperOfData.py"





});
}

$("#showRecords").click(function(){
$.ajax({
type: "GET",
url: "/Users/robberbee/Documents/GitHub/Vertex-Calculator/scrapperOfData.py"





});
beforeWego();
});

function getEquation(part1, part2){
  var create = part1 + part2;
  create = create.split(' ').join('');
  return create;
}
function keeper(update) {

update = update.reduce(getEquation);
var cur = new Date();
///var par = "<p class='importantRec' > " + update + "</br>" + "  Time of Calculation: " + cur.toUTCString()  +"</p>";
var par =  update + " Time of Calculation: " + cur.toUTCString()  + "</br>";
newRecords += par;
document.getElementById("today").innerHTML = newRecords;


///historyLib.getElementById('Records').appendChild(par);
}
  var result = 0.0;
  var equat = [];


  //$('#showRecords').unbind('click').click(function(){


///  })
function clearing() {
equat = [];
document.getElementById("equation").value = equat;
}
$('#calculator tr td').unbind('click').click(function(){
   var keyPressed = this.innerHTML;


if (keyPressed.indexOf("=") >= 0){

   ///result = document.getElementById('equation').innerHTML;
///   var makeEquat = equat.reduce(getEquation);
// result = eval(makeEquat);
var completeEqua = equat;
completeEqua.push(keyPressed);
result = eval(document.getElementById("equation").value);
completeEqua.push(result);
////completeEqua.push("</br>");

keeper(completeEqua);
  document.getElementById("equation").value = result;
  equat = [];
  equat.push(result);
  aj();
}
else if (keyPressed.indexOf("CLEAR") >= 0) {
  clearing();
}
else{
  equat.push(keyPressed);

  document.getElementById("equation").value = equat.reduce(getEquation);
}


})




}
);
///window.addEventListener('beforeunload', function(event) {
function beforeWego() {
///global.sharedRecord = {hist: record}
location.replace("historyUser.html");
///file =fopen("c:\historyUser.html", 3);
//document.open("historyUser.html");
///for (i=0; i < (record.length); i++){
//var theChild = record[i];

//document.write(theChild);
//fs.appendFile( 'CalculationStorage.txt',theChild);

}


//var sending = record.toString();
///exports.recordRelease = function() {
///    return sending;
///};



