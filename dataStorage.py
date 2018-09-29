#from bs4 import BeautifulSoup
import json
calcRecords = list()
oldRecords = list()





#import os
#import re

z = open('historyUser.html', 'w')
historyDisp = """

    <html xmlns="http://www.w3.org/1999/xhtml">
   <script src="https://code.jquery.com/jquery-3.1.1.min.js"> </script>
   <script type="text/javascript" src="calculator.js" type = "module"></script>
   <script type="text/javascript" src="dataStorageScript.js"></script>
   <button onclick="location.href='startingUserCalculator.html'"> Back </button> </br>

   <h1>Records</h1>
   <p id ="Records"></p>

   <script>
   ///var newRecord = require('calculator');
   var ge = require('calculator');

   document.getElementById("Records").innerHTML = ge.recordRelease();
   </script>
   </html>
   for
    """
#soup = open('calculator.js', 'r')
#recording = soup.findAll('<p> ')

z.write(historyDisp)


#soup = open("/Users/robberbee/Documents/GitHub/Vertex-Calculator/calculator.js")

#recording = json.load(soup)
#calcRecords = list(set().union(calcRecords, newList))

#if len(newList) > 0:
    #for r in newList:
        #calcRecords.append(r)



z.close()
from bs4 import BeautifulSoup
with open("historyUser.html", "r") as u:
    content = u.read()
    beautiful = BeautifulSoup(content, 'lxml')
    recording = beautiful.p.find_all('p');
    #pars = recording.string
    newList = []
    for e in recording:
        newList.append[e]
    calcRecords += newList
    calcRecords =set(calcRecords)

#soup.close()
#calculator = open("calculator.js","r")
#finding = calculator.read()

#aEquat = finding.equat
#aResult = finding.result
#recordEquation =[]
#recordResult = []
#def makeRecord(equation, result):
    #recordEquation.append(equation)
    #recordResult.append(result)



#z.write(historyDisp)
