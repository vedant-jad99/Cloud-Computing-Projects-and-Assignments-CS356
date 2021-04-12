from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.html5 import URLField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class Picture(FlaskForm):
    profile = FileField('Add Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    add = SubmitField("Add")

class RegistrationForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    conf_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username is already taken. Please choose a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email is already taken. Please choose a different email.")


class LoginForm1(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    remember = BooleanField("Remember Me")

class LoginForm2(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    remember = BooleanField("Remember Me")

class Info(FlaskForm):
    about = TextAreaField("About")
    link1 = URLField("Link 1")
    link2 = URLField("Link 2")
    link3 = URLField("Link 3")
    link4 = URLField("Link 4")
    profession = StringField("Profession")
    recovery_mail = EmailField("Recovery email")
    done = SubmitField("Done")