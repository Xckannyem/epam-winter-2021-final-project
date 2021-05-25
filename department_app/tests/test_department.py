"""
This module defines the test cases for employee model
"""
# pylint: disable=cyclic-import
from datetime import datetime

# pylint: disable=import-error
from department_app import db
from department_app.models.employee import Department
from department_app.tests.conftest import BaseTestCase


class TestDepartment(BaseTestCase):
    """
    Class for department model test cases
    """
    def test_department_representation(self):
        """
        Testing if the string representation of
        department is correct
        """
        department = Department(name='test_department', description='test')
        db.session.add(department)
        db.session.commit()
        self.assertEqual('Department: test_department', repr(department))

