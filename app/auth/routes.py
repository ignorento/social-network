from app.auth import auth_bp
from flask import render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user
from ..models import User, Profile
from .. import db
from ..services import UserService


user_service = UserService()


@auth_bp.route('/')
def index():
    return "Hello from auth"


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid username/password", category="error")
            return redirect(url_for("auth.login"))

        login_user(user, remember=form.remember.data)

        return redirect(url_for("main.index"))

    return render_template("auth/login.html", form=form)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()

    if form.validate_on_submit():

        username_in_db = User.query.filter_by(username=form.username.data).first()
        email_in_db = User.query.filter_by(username=form.username.data).first()

        if email_in_db:
            flash("This email is already registered, please login!", category="error")
            return render_template("auth/login.html", form=form)

        if username_in_db:
            flash("This username is taken, please select another!", category="error")
            return render_template("auth/register.html", form=form)

        user_service.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,

            first_name=form.first_name.data,
            last_name=form.last_name.data,
            linkedin=form.linkedin.data,
            facebook=form.facebook.data
        )
        # Рефактор теперь єто все перенесено в services
        # user = User(
        #     username=form.username.data,
        #     email=form.email.data
        # )
        # user.set_password(form.password.data)
        #
        # db.session.add(user)
        # db.session.commit()
        #
        # profile = Profile(
        #     user_id=user.id,
        #     first_name=form.first_name.data,
        #     last_name=form.last_name.data,
        #     linkedin=form.linkedin.data,
        #     facebook=form.facebook.data
        # )
        #
        # db.session.add(profile)
        # db.session.commit()

        flash(f"Successfully registered {form.data['username']}! Profile was created", category="success")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
