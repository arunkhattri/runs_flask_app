#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

runs = [
    {"date": "2022-05-02", "km": 5.32, "time": "00:27:35"},
    {"date": "2022-05-05", "km": 4.32, "time": "00:22:15"},
    {"date": "2022-06-01", "km": 2.52, "time": "00:17:20"},
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", runs=runs)


@app.route("/records")
def personal_records():
    return render_template("records.html")


@app.route("/year-at-a-glance")
def year_at_a_glance():
    return render_template("year.html")


@app.route("/current-month")
def current_month():
    return render_template("current_month.html")


if __name__ == "__main__":
    app.run(debug=True)
