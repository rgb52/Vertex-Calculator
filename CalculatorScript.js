
var record = [];
$(document).ready(function(){
function getEquation(part1, part2){
  var create = part1 + part2;
  create = create.split(' ').join('');
  return create;
}
function keeper(update) {
update = update.reduce(getEquation);
var cur = new Date();
var par = "<p>" + update + "</br>" + "  Time of Calculation: " + cur.toUTCString()  +"</p> </br>";

record.push(par);

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
document.open('historyUser.html');
for (i=0; i < (record.length); i++){
var theChild = record[i];
document.write(theChild);

}
var sending = record.toString();
///exports.recordRelease = function() {
///    return sending;
///};

}

