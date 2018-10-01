from bs4 import BeautifulSoup
from dataStorage import historyDisp
with open("historyUser.html", "w") as ip:
    ip.write("The surge 2 please")
newList = list()
completeCal

def gettingOldData():
    #droup = BeautifulSoup(open("historyUser.html", "r"), "html.parser")
    droup = BeautifulSoup("historyUser.html", "html.parser")
    oldDiv = droup.div("target")
    newCal = oldDiv
    droup.close()
    return oldCal

def gettingData():
    soup = BeautifulSoup(open("startingUserCalculator.html", "r"), "html.parser")
    #beautiful = BeautifulSoup(u, 'html.parser')
    #content = soup.read()
    #soup = BeautifulSoup(content, 'lxml')
    theDiv = soup.find_element_by_id(id ="today")
    newCal = theDiv
    oldCal = gettingOldData()
    #pars = recording.string
    #for e in recording:
        #newList.add(e)
    soup.close()
    return newCal + oldCal

##completeCal = gettingData()
def testingMachine():
    if len(completeCal)>0:
        return true
    else:
        return false

def displayingData():
    y = open("historyUser.html", "w")
    y.write(len(completeCal))
    #y.write(completeCal)
    #y.write(historyDisp)
    if testingMachine():
        y.write("Success!!")
    else
        y.write("Failure!!!")
    y.write("Testing this right now")
    y.write("Please work please work")
    y.close

#displayingData()
with open("historyUser.html", "w") as y:
    #y.write(len(completeCal))
    #y.write(completeCal)
    #y.write(historyDisp)
    y.write("Please Work!!!!")

def keepingHistory():
    file = open("pastActivity.txt","w")
    keeping.write(completeCal)
    file.close()
#keepingHistory()
