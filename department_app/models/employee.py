"""
This module consists of the class Employee to work with `employees` table
"""
# pylint: disable=cyclic-import
from datetime import date

# pylint: disable=import-error
from flask_login import UserMixin

from department_app import db, login_manager
from department_app import bcrypt

from .department import Department


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=60), nullable=False, unique=True)
    email = db.Column(db.String(length=60), nullable=False, unique=True)
    first_name = db.Column(db.String(length=60), nullable=False)
    last_name = db.Column(db.String(length=60), nullable=False)
    password_hash = db.Column(db.String(length=128), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    salary = db.Column(db.Integer)
    birthday = db.Column(db.Date)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('Password is not readable attribute.')

    @password.setter
    def password(self, plain_text_password):
        """
        Set password to a hashed password
        """
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        """
        Check if hashed password matches actual password
        :return: `True` or `False`
        """
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    # pylint: disable=no-self-use
    def calculate_age(self, birth):
        """
        Calculate the age of an employee by date of birth
        :return: the age of the employee
        """
        today = date.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def to_dict(self):
        """
        Serializer that returns a dictionary from its fields
        :return: the employee in json format
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'department': Department.query.get_or_404(self.department_id).name,
            'salary': self.salary,
            # pylint: disable=no-member
            'birthday': self.birthday.strftime('%m/%d/%Y')
        }

    def __repr__(self):
        """
        Representation of the employee
        :return: a string representing the employee by username
        """
        return f'Employee: {self.username}'


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    """
    :param user_id:
    :return:
    """
    return Employee.query.get(int(user_id))
