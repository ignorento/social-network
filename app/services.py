from app import db
from app.models import User, Profile, Post
from app.schemas import UserSchema, PostSchema


class UserService:

    def get_by_id(self, user_id):
        user = db.session.query(User).filter(User.id == user_id).first_or_404()
        return user

    def get_by_username(self, username):
        user = db.session.query(User).filter(User.username == username).first_or_404()
        return user

    def create(self, **kwargs):  # data
        user = User(username=kwargs.get('username'), email=kwargs.get('email'))  # data
        user.set_password(kwargs.get('password'))

        db.session.add(user)
        db.session.commit()

        profile = Profile(
            user_id=user.id,
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'),
            linkedin=kwargs.get('linkedin'),
            facebook=kwargs.get('facebook')
        )
        db.session.add(profile)
        db.session.commit()

        return user

    def update(self, data):
        user = self.get_by_id(data['id'])
        data['profile']['id'] = user.profile.id
        data['profile']['user_id'] = user.id

        user = UserSchema(exclude=('password',)).load(data)
        db.session.add(user)
        db.session.commit()

        return user

    def delete(self, user_id):
        user = self.get_by_id(user_id)
        profile = user.profile
        db.session.delete(profile)
        db.session.commit()

        db.session.delete(user)
        db.session.commit()

        return True


class PostService:

    def get_by_id(self, post_id):
        post = db.session.query(Post).filter(Post.id == post_id).first_or_404()
        return post

    def update(self, data):
        my_post = PostSchema().load(data)
        db.session.add(my_post)
        db.session.commit()

        return my_post

    def delete(self, post_id):
        post = self.get_by_id(post_id)
        db.session.delete(post)
        db.session.commit()
        return True

    def create(self, **kwargs):  # data
        post = Post(title=kwargs.get('title'), content=kwargs.get('content'), author_id=kwargs.get('author_id'))  # data

        db.session.add(post)
        db.session.commit()

        return post
