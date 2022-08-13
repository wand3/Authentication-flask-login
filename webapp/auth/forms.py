from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(Form):
    # email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username_or_email = StringField('Username or email')
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 30), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 30)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')
                             , Length(min=6, message='Passwords must be at least 6')])
    confirm = PasswordField('Confirm password', validators=[DataRequired()])
    agree = BooleanField('I Agree')
    submit = SubmitField('Register')

