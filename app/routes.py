from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    contex = {
        "user" : {"username": "babin"},
        "title" : "Hillel"
    }
    return render_template("index.html", **contex)
