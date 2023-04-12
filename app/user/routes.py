from app.user import user_bp
from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required

from app.user.forms import ProfileForm

from .. import db
from ..models import User, Post
from ..post.forms import PostForm


@user_bp.route("/blog")
@login_required
def blog():
    form = PostForm()
    posts = (
        db.session.query(Post)
        .filter(
            Post.author_id == current_user.id
        )
        .order_by(Post.created_at.desc())
        .all()
    )
    return render_template("user/blog.html", posts=posts, form=form)


@user_bp.route("/profile/<string:username>", methods=['GET', 'POST'])
@login_required
def profile(username):
    user = db.session.query(User).filter(User.username == username).first_or_404()
    form = ProfileForm()
    if form.validate_on_submit():

        user.profile.first_name = form.first_name.data
        user.profile.last_name = form.last_name.data
        user.profile.linkedin = form.linkedin.data
        user.profile.facebook = form.facebook.data
        user.profile.bio = form.bio.data
        db.session.commit()
        flash('Your changes have been saved!', category="success")
        return redirect(url_for('user.profile', username=user.username))
    elif request.method == 'GET':
        form.first_name.data = user.profile.first_name
        form.last_name.data = user.profile.last_name
        form.linkedin.data = user.profile.linkedin
        form.facebook.data = user.profile.facebook
        form.bio.data = user.profile.bio
    return render_template('user/profile.html', user=user, form=form)
