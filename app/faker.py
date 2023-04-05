import click
from flask import Blueprint
from faker import Faker

from app import db
from app.models import User

faker_bp = Blueprint('fake', __name__)
faker = Faker()


@faker_bp.cli.command("users")
@click.argument('num', type=int)
def users(num):
    ''' Create 'num' of fake users '''
    users = []
    for i in range(num):
        # generate fake username and email
        username = faker.user_name()
        email = faker.email()

        # get user by username and email
        user = (
            db.session.query(User)
            .filter(
                User.username == username,
                User.email == email
            )
        ).first()

        # no such user in db yet --> insert
        if not user:
            user = User(
                username=username,
                email=email,
            )
            db.session.add(user)
            users.append(user)

    # save changes in db
    db.session.commit()
    print(num, 'user added.')
