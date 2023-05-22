from pathlib import Path

import pandas as pd

from flask import Blueprint

import config
from .. import db
from ..models import Profile, User, Post
from sqlalchemy import func

user_bp = Blueprint('user', __name__, url_prefix='/user')

from . import routes  # noqa


@user_bp.cli.command('user_command')
def user_command():

    user_info = (
        db.session.query(Profile.full_name, User.email)
        .join(Profile, Profile.user_id == User.id)
        .all()
    )

    print(user_info)


@user_bp.cli.command('extract_users')
def extract_users():

    users_info = (
        db.session.query(
            User.username,
            User.email,
            Profile.full_name,
            func.count(Post.author_id)
        )
        .join(Profile, Profile.user_id == User.id)
        .outerjoin(Post, Post.author_id == User.id)
        .group_by(User.username, User.email, Profile.full_name,)
        .all()
    )

    # print(users_info)
    df = pd.DataFrame(users_info, columns=['username', 'email', 'full_name', 'кількість постів'])
    df.to_csv(Path(config.basedir)/'users.csv')
    print('File users.csv successfully created. Nice work!')
