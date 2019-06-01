import json

from flask import Flask, render_template
from datetime import date, datetime

app = Flask(__name__)

all_entries = []


@app.before_first_request
def load_portfolio_entries():
    global all_entries
    with app.open_resource("portfolio.json") as f:
        all_entries = json.loads(f.read())


@app.route('/')
def portfolio():
    days = (datetime.now().date()-date(2002, 11, 21)).days
    age = {"days": days, "years": round(days/365.2425, 1)}
    return render_template("portfolio.html", entries=all_entries, age=age)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
