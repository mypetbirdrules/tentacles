from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="A well built web page")

@app.route("/index")
def index2():
    return redirect(url_for("index"))

@app.route("/home")
def home():
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html", title="The About Page")

if __name__ == "__main__":
    app.run()
