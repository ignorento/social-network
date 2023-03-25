from app.main import main_bp
from flask import render_template

@main_bp.route("/")
@main_bp.route("/index")
def index():
    contex = {
        "user" : {"username": "babin"},
        "title" : "Hillel"
    }
    return render_template("index.html", **contex)

@main_bp.route("/about")
def about():
    return render_template("about.html")
