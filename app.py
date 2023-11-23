from flask import Flask, request
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Today is {date.today().strftime('%d/%m/%Y')}</p>"
