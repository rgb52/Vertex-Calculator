
import json
from bs4 import BeautifulSoup
from flask import Flask
from calculator import contentRec
#contentRec = set()
calcRecords = set()
oldRecords = list()





#import os
#import re

z = open('historyUser.html', 'a')
historyDisp = """
    Content-Type: "text/plain"
    <html xmlns="http://www.w3.org/1999/xhtml" Content-Type: "text/plain">


   <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>


   <script type="text/javascript" src="calculator.js" type = "module"> </script>
   <script type="text/javascript" src="dataStorageScript.js" type = "module"></script>
<meta charset=utf-8>

   <h1>Records</h1>
   <body>
    <center> <button type ="button" onclick="location.href='startingUserCalculator.html'"> Back </button></center> </br>
   <div id ="Records"><p></p></div>

   </body>
   <script>
   ///var newRecord = require('./calculator');


$(document).ready(function(){
///var ge = require('./calculator');
///alert("Here its activated");
///document.getElementById("Records").innerHTML = ge.recordRelease();
}
);
   </script>
   </html>
   for
    """

#soup = open('calculator.js', 'r')
#recording = soup.findAll('<p> ')

#z.write(historyDisp)

srt = repr(contentRec)
#z.write(srt)



#soup = open("/Users/robberbee/Documents/GitHub/Vertex-Calculator/calculator.js")

#recording = json.load(soup)
#calcRecords = list(set().union(calcRecords, newList))

#if len(newList) > 0:
    #for r in newList:
        #calcRecords.append(r)



z.close()


soup = BeautifulSoup(open("startingUserCalculator.html", "r"), "html.parser")
    #beautiful = BeautifulSoup(u, 'html.parser')
recording = soup.find_all('p')
    #pars = recording.string


newList = set()
for e in recording:
    newList.add(e)
calcRecords = calcRecords.union(newList)

calcRecords = set(calcRecords)
completeList = calcRecords.difference(newList)
#creatIng = calcRecords.values()


recordFile = open("CalculationStorage.txt", "a")

for y in completeList:
    print(y)
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
