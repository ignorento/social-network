import datetime

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


class TimestampMixin:
    created_at = db.Column(db.DateTime, default=datetime)


class User(BaseModel, UserMixin):

    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"{self.username}({self.email})"


class Profile(db.Model):
    __tablename__ = "profiles"
    __table_args__ = (
        db.Index("idx-profiles_user_id", "user_id"),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", name="fk_profiles_user_id"),
        nullable=False
    )
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    linkedin = db.Column(db.String)
    facebook = db.Column(db.String)

    bio = db.Column(db.String)

    user = db.relationship("User", backref=db.backref("profile", uselist=False), uselist=False)
