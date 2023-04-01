from app.auth import auth_bp
from flask import render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm

@auth_bp.route('/')
def index():
    return "Hello from auth"

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Submitted username={form.data['username']}, remember={form.data['remember']}", category="success")
        return redirect(url_for("main.index"))
    return render_template("auth/login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"Registered Username={form.data['username']}, Email={form.data['email']}", category="success")
        return redirect(url_for("main.index"))
    return render_template("auth/register.html", form=form)