from flask import Flask, request
# Import datetime class from datetime module
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
 
    dayofweek=""
    # returns current date and time
    numdayofweek = datetime.now().weekday()
    if (numdayofweek == 0): dayofweek="Monday"
    if (numdayofweek == 1): dayofweek="Tuesday"
    if (numdayofweek == 2): dayofweek="Wednesday"
    if (numdayofweek == 3): dayofweek="Thursday"
    if (numdayofweek == 4): dayofweek="Friday"
    if (numdayofweek == 5): dayofweek="Saturday"
    if (numdayofweek == 6): dayofweek="Sunday"
    #print("**********")
    now = datetime.now().strftime("Today:  "+""+dayofweek+"  "+"%d/%m/%Y"+""+"Time:  "+""+"%H:%M:%S")
    #print(now)
    #print("**********")

    return now
    
