#from bs4 import BeautifulSoup
import json
from calculator import *
from bs4 import BeautifulSoup

calcRecords = set()
oldRecords = list()





#import os
#import re

z = open('historyUser.html', 'w')
historyDisp = """

    <html xmlns="http://www.w3.org/1999/xhtml">
      <center> <button type ="button" > "Back" </button></center> </br>

   <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>


   <script type="text/javascript" src="calculator.js" type = "module"> </script>
   <script type="text/javascript" src="dataStorageScript.js" type = "module"></script>

   <h1>Records</h1>
   <div id ="Records"><p></p></div>

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

z.write(historyDisp)
srt = repr(contentRec)
z.write(srt)


#soup = open("/Users/robberbee/Documents/GitHub/Vertex-Calculator/calculator.js")

#recording = json.load(soup)
#calcRecords = list(set().union(calcRecords, newList))

#if len(newList) > 0:
    #for r in newList:
        #calcRecords.append(r)



z.close()


soup = BeautifulSoup(open("historyUser.html", "r+"), "html.parser")
    #beautiful = BeautifulSoup(u, 'html.parser')
recording = soup.find_all('p')
    #pars = recording.string
newList = set()
for e in recording:
    newList.add(e)
calcRecords += newList

calcRecords =set(calcRecords)
completeList = calcRecords.difference(newList)
#creatIng = calcRecords.values()
for i in completeList:
    print(i)


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
