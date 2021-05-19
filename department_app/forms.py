"""
form.py file of forms module for storing web form classes
"""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# pylint: disable=relative-beyond-top-level
from .models.employee import Employee
from .models.department import Department


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

    # pylint: disable=no-self-use
    def validate_username(self, username_to_check):
        """
        Username validation function
        """
        user = Employee.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist! Please try a different username')

    def validate_email(self, email_to_check):
        """
        Email validation function
        """
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


class DepartmentForm(FlaskForm):
    """
    Form to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class EmployeeForm(FlaskForm):
    """
    Form to add or edit an employee
    """
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    birthday = StringField('Birthday', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


# pylint: disable=unnecessary-lambda
class EmployeeAssignForm(FlaskForm):
    """
    Form to assign departments to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    submit = SubmitField(label='Submit')
