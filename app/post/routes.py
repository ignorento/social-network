from app import db
from app.post import post_bp
from app.post.forms import PostForm
from app.models import Post, Like, Dislike
from flask import redirect, url_for, render_template, flash, request, abort
from flask_login import login_required, current_user

from app.services import PostService

post_service = PostService()


@post_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            post_service.create(
                title=form.title.data,
                content=form.content.data,
                author_id=current_user.id
            )
            # Рефактор теперь все происходит в сервисах
            # post = Post(title=form.title.data, content=form.content.data, author=current_user)
            #
            # db.session.add(post)
            # db.session.commit()
            flash('Your post has been created!', 'success')
        else:
            title = form.title.data
            content = form.content.data

            if not title or len(title) < 2:
                flash('Title must be at least 3 characters log', category='error')

            if not content or len(content) < 10:
                flash('Content must be at least 10 characters log', category='error')

        return redirect(url_for("user.blog"))
    return render_template('user/blog.html', title='Create Post', form=form)


@post_bp.route('/<int:post_id>/like', methods=['GET', 'POST'])
@login_required
def like(post_id):
    # Get the post by id from the database
    post = Post.query.get_or_404(post_id)

    # Check if the user has already liked the post
    if Like.query.filter_by(user=current_user, post=post).count() > 0:
        flash('You have already liked this post!', 'warning')
    else:
        # Create a new like object
        like_post = Like(user=current_user, post=post)
        # Add the like to the database
        db.session.add(like_post)
        db.session.commit()
        flash('You have liked this post!', 'success')
    return redirect(request.referrer)


@post_bp.route('/<int:post_id>/dislike', methods=['GET', 'POST'])
@login_required
def dislike(post_id):
    post = Post.query.get_or_404(post_id)

    if Dislike.query.filter_by(user=current_user, post=post).count() > 0:
        flash('You have already disliked this post!', 'warning')
    else:
        # Create a new dislike object
        dislike_post = Dislike(user=current_user, post=post)

        db.session.add(dislike_post)
        db.session.commit()
        flash('You have disliked this post!', 'success')
    return redirect(request.referrer)


@post_bp.route('/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('user.blog'))
