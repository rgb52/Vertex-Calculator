#from bs4 import BeautifulSoup
import json
#import os
#import re

z = open('historyUser.html', 'w')
historyDisp = """
    $ Python dataStorage.py
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
#soup = open('calculator.js', 'r')
#recording = soup.findAll('<p> ')

soup = BeautifulSoup(historyUser.html)

#soup = open("/Users/robberbee/Documents/GitHub/Vertex-Calculator/calculator.js")
recording = soup.find_all('p')
newList = [e.text for e in recording]
#recording = json.load(soup)
calcRecords = list(set().union(calcRecords, newList))
if len(newList) > 0:
    for r in newList:
        calcRecords.append(r)


for z in calcRecords:
    print(z)

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
soup.close()
