from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    EmailField,
    URLField,
    validators
)


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired(message="Username is required")])
    password = PasswordField(
        "Password",
        validators=[
            validators.DataRequired(message="Password is required"),
            validators.Length(min=6, message="min 6 length of password is required")
        ]
    )
    remember = BooleanField("Remember")
    submit = SubmitField("Log In")


class RegisterForm(LoginForm):
    email = EmailField("Email", validators=[validators.DataRequired(message="Email is required"), validators.Email()])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            validators.DataRequired(message="Confirm password is required"),
            validators.EqualTo("password", message="Passwords should match")
        ]
    )
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    linkedin = URLField("Linkedin URL", validators=[validators.URL(message="This is not URL"), validators.Optional()])
    facebook = StringField("Facebook URL", validators=[validators.URL(message="This is not URL"), validators.Optional()]) # noqa
    submit = SubmitField("Register")
