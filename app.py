from unicodedata import name
from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)

con = sqlite3.connect("bday.db", check_same_thread=False)
cur = con.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods = ["POST"])
def add():
    name = request.form.get('name')
    date = request.form.get('date')
    con.execute("INSERT INTO bday (name, date) VALUES (?, ?);", (name, date))
    con.commit()
    return redirect("/bday")

@app.route("/bday")
def bd():
    b_day = cur.execute('SELECT * FROM bday').fetchall()
    return render_template("success.html", bd = b_day)