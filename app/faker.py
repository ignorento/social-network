import click
from flask import Blueprint
from faker import Faker

from app import db
from app.models import User, Profile

faker_bp = Blueprint('fake', __name__)
faker = Faker()


@faker_bp.cli.command("users")
@click.argument('num', type=int)
def users(num):
    ''' Create 'num' of fake users '''
    users_pass = []
    for i in range(num):
        # generate fake username and email
        username = faker.user_name()
        email = faker.email()
        password = faker.password()

        first_name = faker.first_name()
        last_name = faker.last_name()
        id_number = faker.unique.random_number(digits=5)
        linkedin_url = f"https://www.linkedin.com/in/{first_name.lower()}-{last_name.lower()}-{id_number}/"
        id_number = faker.unique.random_number(digits=5)
        facebook_url = f"https://www.facebook.com/{first_name.lower()}.{last_name.lower()}.{id_number}/"

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
            user.set_password(password)

            db.session.add(user)
            db.session.commit()

            users_pass.append([username, password])

            profile = Profile(
                user_id=user.id,
                first_name=first_name,
                last_name=last_name,
                linkedin=linkedin_url,
                facebook=facebook_url
            )

            db.session.add(profile)
            db.session.commit()

    # save changes in db
    # db.session.commit()
    print(num, 'user added.')
    # for me Login
    print(users_pass)
