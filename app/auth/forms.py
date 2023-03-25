from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    EmailField,
    validators
)


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=6)])
    remember = BooleanField("Remember")
    submit = SubmitField("Log In")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    email = EmailField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=6)])
    submit = SubmitField("Register")