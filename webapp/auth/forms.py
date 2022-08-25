from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from ..models import User
import re


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
    
    #validators
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

    def validate_password(self, password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?_&.])[A-Za-z\d@$!_#%*.?&]{5,30}$"
        pat = re.compile(reg)
        # searching regex
        mat = re.search(pat, password.data)

        # validating conditions
        if mat:
            pass
        else:
            raise ValidationError("Password must contain Uppercase, Lowercase, Numbers and Symbols")
