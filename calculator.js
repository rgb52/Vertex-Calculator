$(document).ready(function(){
  var result = 0.0;
  var equat = [];
  //$('#showRecords').unbind('click').click(function(){
    

///  })
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

result = eval(document.getElementById("equation").value)
   document.getElementById("equation").value = result;
}
else if (keyPressed.indexOf("CLEAR") >= 0) {
  equat = [];
  document.getElementById("equation").value = equat;
}
else{
  equat.push(keyPressed);

  document.getElementById("equation").value = equat.reduce(getEquation);
}


})




}
);
