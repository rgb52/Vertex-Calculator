#from bs4 import BeautifulSoup
#import json
#import os
#import re
z = open('historyUser.html', 'w')
historyDisp = """
    <html xmlns="http://www.w3.org/1999/xhtml">
   <script src="https://code.jquery.com/jquery-3.1.1.min.js"> </script>
   <script type="text/javascript" src="calculator.js"></script>
   <button onclick="location.href='startingUserCalculator.html'"> Back </button> </br>

   <h1>Records</h1>
   <p id ="Records"></p>
   <script>
   for(var i = 0; i <record.length; i++){
   document.getElementById("Records").innerHTML = record[i];
   }
   </script>

   </html>
    """

#calculator = open("calculator.js","r")
#finding = calculator.read()

#aEquat = finding.equat
#aResult = finding.result
#recordEquation =[]
#recordResult = []
#def makeRecord(equation, result):
    #recordEquation.append(equation)
    #recordResult.append(result)



z.write(historyDisp)
z.close()
