
var record = [];
$(document).ready(function(){
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
function getEquation(part1, part2){
  var create = part1 + part2;
  create = create.split(' ').join('');
  return create;
}

if (keyPressed.indexOf("=") >= 0){

   ///result = document.getElementById('equation').innerHTML;
///   var makeEquat = equat.reduce(getEquation);
// result = eval(makeEquat);
var completeEqua = equat;
completeEqua.push(keyPressed);
result = eval(document.getElementById("equation").value);
completeEqua.push(result);
completeEqua.push("</br>");
completeEqua.reduce(getEquation);
record.push(completeEqua);



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
window.addEventListener('beforeunload', function(event) {

var sending = record.toString();
recordRelease = function() {
    return sending;
};

}
);
