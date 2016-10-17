#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for, g, sessions
from tentacles import app
import sqlite3
import sys
import os

# call on server start - good for testing and portability
def tryInitDB(dbPath):
    try:
        dbCon = sqlite3.connect(dbPath)
        dbCursor = dbCon.cursor()
        dbCursor.execute("CREATE TABLE pr0n IF NOT EXISTS pr0n(postTitle TEXT, postDescription TEXT, )")
    except:
        sys.stderr.write("[FATAL] Error initializing connection to database\n")
        sys.stderr.write("Perhaps a faulty file path in config?\n")
        sys.stderr.write("Forcing exit from fatal error\n")
        # exit with failure return value
        sys.exit(1)

def connectDB(dbPath):
    try:
        dbCon = sqlite3.connect(dbPath)
        dbCursor = dbCon.cursor()
        return (dbCon, dbCursor)
    except:
        return False

def closeDBCon(dbConnectionSessionTuple):
    try:
        dbConnectionSessionTuple[1].commit()
        dbConnectionSessionTuple[1].close()

        dbConnectionSessionTuple[0].commit()
        dbConnectionSessionTuple[0].close()
    except:
        return False



# initialize web server
# initialize non-created database IF NOT EXISTS
tryDBInit(os.path.join())

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
