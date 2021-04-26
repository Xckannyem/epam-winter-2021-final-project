from flask_login import UserMixin

from department_app import db, login_manager
from department_app import bcrypt


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=60), index=True, nullable=False, unique=True)
    email = db.Column(db.String(length=60), index=True, nullable=False, unique=True)
    first_name = db.Column(db.String(length=60), index=True, nullable=False)
    last_name = db.Column(db.String(length=60), index=True, nullable=False)
    password_hash = db.Column(db.String(length=128), index=True, nullable=False,)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

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
        """
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'Employee: {self.username}'


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def __repr__(self):
        return f'Department: {self.name}'


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'Role: {self.name}'
