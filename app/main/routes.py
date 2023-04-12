from app import db
from app.main import main_bp
from flask import render_template
from app.models import Post


@main_bp.route("/")
@main_bp.route("/index")
def index():
    posts = db.session.query(Post).order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts)

    # users_data = [
    #     {
    #         "username": "oleh",
    #         "email": "oleh@gmail.com"
    #     },
    #     {
    #         "username": "valik",
    #         "email": "valik@gmail.com"
    #     },
    #     {
    #         "username": "tonya",
    #         "email": "tonya@gmail.com"
    #     },
    #     {
    #         "username": "orest",
    #         "email": "orest@gmail.com"
    #     },
    # ]
    # for u in users_data:
    #     user = (
    #         db.session.query(User)
    #         .filter(
    #             User.username == u.get("username"),
    #             User.email == u.get("email")
    #         ).first()
    #     )
    #     if user:
    #         continue
    #
    #     user = User(
    #         username=u.get('username'),
    #         email=u.get('email')
    #     )
    #     db.session.add(user)
    # db.session.commit()


@main_bp.route("/about")
def about():
    return render_template("about.html")
