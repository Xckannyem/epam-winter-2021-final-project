from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models.auth_model import Employee


class RegisterForm(FlaskForm):
    """
    Form for users to create new account
    """
    username = StringField(label='User Name', validators=[Length(min=3, max=30), DataRequired()])
    email = StringField(label='Email Address', validators=[DataRequired(), Email()])
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='First Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[
                                                            EqualTo('password'),
                                                            DataRequired()
                                                            ])
    submit = SubmitField(label='Create Account')

    def validate_username(self, username_to_check):
        user = Employee.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist! Please try a different username')

    def validate_email(self, email_to_check):
        email = Employee.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exist! Please try a different email')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField(label='Email:', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
