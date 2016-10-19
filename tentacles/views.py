#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for, g, sessions, request
from tentacles import app
import sqlite3
import sys
import os


globalDatabasePath = os.path.join(app.root_path, "database/posts.sqlite3")

# call on server start - good for testing and portability
def tryInitDB(dbPath):
    try:
        dbCon = sqlite3.connect(dbPath)
        dbCursor = dbCon.cursor()
        # long-ass SQL query
        dbCursor.execute("CREATE TABLE IF NOT EXISTS pr0n(postTitle TEXT, postDescription TEXT, category1 TEXT, category2 TEXT, category3 TEXT, sha256hash TEXT, yearUploaded SMALLINT, monthUploaded TINYINT, dayUploaded TINYINT, upCount BIGINT, downCount BIGINT);")
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
        # save and stop dbCursor
        dbConnectionSessionTuple[1].commit()
        dbConnectionSessionTuple[1].close()

        # save and stop dbCon
        dbConnectionSessionTuple[0].commit()
        dbConnectionSessionTuple[0].close()
    except:
        return False

def searchQueryDB(dbConTuple, searchString, categoryFilter1, categoryFilter2, categoryFilter3, resultLimit):
    searchTermList = searchString.split(" ")
    resultSet = []

    for searchTerm in searchTermList:
        resultSet = resultSet + dbConTuple[1].execute("SELECT postTitle, postDescription, category1, category2, category3, sha256hash, yearUploaded, monthUploaded, dayUploaded, upCount, downCount FROM pr0n WHERE (postTitle LIKE "%?%" AND postDescription LIKE )")

# initialize web server
# initialize non-created database if it doesn't exist
tryInitDB(globalDatabasePath)

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

@app.route("/search/", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search_string = request.form["video-search"]
        print(search_string)
    else:
        print("Display results below!")
    
    return render_template("search.html", title="Search Videos")
