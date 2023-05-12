from pathlib import Path
import config
import pandas as pd
from .. import db
from ..models import Like, Dislike, User, Post
from sqlalchemy import func
import click

from flask import Blueprint

post_bp = Blueprint('post', __name__, url_prefix='/post')

from . import routes  # noqa


@post_bp.cli.command('exctract_posts')
@click.argument('user_id', type=int)
def exctract_posts(user_id):
    my_user = db.session.query(User).filter(User.id == user_id).first()
    if my_user:
        my_posts = (
            db.session.query(
                Post.title,
                func.count(func.distinct(Like.user_id)),
                func.count(func.distinct(Dislike.user_id)),
                Post.created_at
            )
            .outerjoin(Like, Like.post_id == Post.id)
            .outerjoin(Dislike, Dislike.post_id == Post.id)
            .filter(Post.author_id == user_id)
            .group_by(Post.title, Post.created_at)
            .all()
        )
        # print(my_posts)
        df = pd.DataFrame(my_posts, columns=['Post Title', 'Likes count', 'Dislikes count', 'Post Created at'])
        df.to_csv(Path(config.basedir) / f'{user_id}_posts.csv')
        print(f'File {user_id}_posts.csv successfully created. Nice work!')
    else:
        print(f"We don't have user id - {user_id}. Please try again!")
