#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for
from tentacles import app

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
