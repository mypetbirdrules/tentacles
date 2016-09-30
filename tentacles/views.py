#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for
from tentacles import app
import sqlite3

def connectDB(dbPath):
    try:
        dbCon = sqlite3.connect(dbPath)
        dbCursor = dbCon.cursor()
        return (dbCon, dbCursor)
    except:
        return False

def closeDBCon(dbConnectionObj):
    try:
        dbConnectionObj.commit()
        dbConnectionObj.close()
    except:
        return False

@app.route("/")
def index():
    return render_template("index.html", title="The Tentacle Project")

@app.route("/index")
def index2():
    return redirect(url_for("index"))

@app.route("/home")
def home():
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html", title="About Project Tentacles")

@app.route("/upload")
def upload():
    return render_template("upload.html", title="Upload Video")
