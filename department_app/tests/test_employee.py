"""
This module defines the test cases for employee model
"""
# pylint: disable=cyclic-import
from datetime import datetime

# pylint: disable=import-error
from department_app import db
from department_app.models.employee import Employee
from department_app.tests.conftest import BaseTestCase


class TestEmployee(BaseTestCase):
    """
    Class for employee model test cases
    """
    def test_employee_representation(self):
        """
        Testing if the string representation of
        employee is correct
        """
        date = datetime.strptime('06/10/1998', '%m/%d/%Y').date()
        employee = Employee(
            username='test_username',
            email='test_email',
            first_name='test_first_name',
            last_name='test_last_name',
            password='test1234',
            salary=100,
            birthday=date
        )
        db.session.add(employee)
        db.session.commit()
        self.assertEqual('Employee: test_username', repr(employee))
