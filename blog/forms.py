from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo,Length
from .models import User

class LoginForm(FlaskForm):
    """User Login Form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    """User Signup Form."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(min=6), Email(message="Enter a valid email.")])
    password = PasswordField('Password', validators=[DataRequired(message="Please enter a password."),Length(min=6, message="Select a stronger password.")])
    password2 = PasswordField(
        'Confirm Your Password', validators=[DataRequired(), EqualTo("password", message="Passwords must match.")])
    submit = SubmitField('Signup!')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
