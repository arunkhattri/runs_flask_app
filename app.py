#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

runs = [
    {"year": "2022", "km": 365.32, "time": "25:27:35"},
    {"year": "2021", "km": 254.32, "time": "15:22:15"},
    {"year": "2020", "km": 182.52, "time": "10:17:20"},
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
