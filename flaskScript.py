from flask import Flask, render_template
app = Flask(__name__)

@app.route('/Users/robberbee/Documents/GitHub/Vertex-Calculator')
def index():
  return render_template('startingUserCalculator.html')

@app.route('/Users/robberbee/Documents/GitHub/historyUser.html')
def my_link():

    r = open("historyUser.html", "a")
    print("It works")
    soup = BeautifulSoup(open("startingUserCalculator.html", "r"), "html.parser")
      #beautiful = BeautifulSoup(u, 'html.parser')
    recording = soup.find_all('p')
      #pars = recording.string
    newList = set()
    for e in recording:
      newList.add(e)
    for s in newList:
        r.write(s)
    r.close()
    return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)
