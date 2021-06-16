"""
This module defines the test cases for department service
"""
# pylint: disable=cyclic-import
from datetime import datetime

# pylint: disable=import-error
from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app.service import department_service
from department_app.tests.conftest import BaseTestCase


class TestDepartmentService(BaseTestCase):
    """
    This is the class for department service test cases
    """

    def test_get_all_departments(self):
        """
        Testing get_all_departments by adding new departments with
        the specified parameters and checks if the count of records is equal to 2
        """
        department1 = Department(name='department1', description='description1')
        department2 = Department(name='department2', description='description2')
        # pylint: disable=no-member
        db.session.add(department1)
        db.session.add(department2)
        db.session.commit()
        self.assertEqual(2, len(department_service.get_all_departments()))

    def test_add_department(self):
        """
        Testing add_department by adding a new department with
        the specified parameters and checks if the count of records is equal to 1
        """
        department_service.add_department(name='New department', description='New description')
        self.assertEqual(1, Department.query.count())

    def test_update_department(self):
        """
        Testing update_department by adding a new department with
        the specified parameters and updates them by new records
        """
        department = Department(name='department1', description='description1')
        # pylint: disable=no-member
        db.session.add(department)
        db.session.commit()
        department_service.update_department(1, name='new name', description='new description')
        department = Department.query.get(1)
        self.assertEqual('new name', department.name)
        self.assertEqual('new description', department.description)

    def test_delete_department(self):
        """
        Testing delete_department by adding a new department with
        the specified parameters, deletes it and checks if the count of records is equal to 1
        """
        department = Department(name='department1', description='description1')
        # pylint: disable=no-member
        db.session.add(department)
        db.session.commit()
        department_service.delete_department(1)
        self.assertEqual(0, Department.query.count())

    def test_get_department_by_id(self):
        """
        Testing get_all_departments by adding a new department with
        the specified parameters and checks if the department id is equal to 1
        """
        department = Department(name='department1', description='description1')
        # pylint: disable=no-member
        db.session.add(department)
        db.session.commit()
        self.assertEqual(1, department_service.get_department_by_id(1)['id'])

    def test_get_average_salary(self):
        """
        Testing the average_salary by department by adding a new department and employees
        and compares the received value with the given one.
        If they are equal then the test is successful
        """
        department = Department(name='test_department_salary', description='test')
        # pylint: disable=no-member
        db.session.add(department)
        date1 = datetime.strptime('10/06/1998', '%m/%d/%Y').date()
        date2 = datetime.strptime('06/10/1991', '%m/%d/%Y').date()
        employee1 = Employee(username='user1',
                             email='test1@gmail.com',
                             first_name='test_first_name',
                             last_name='test_last_name',
                             password='test1234',
                             department_id=1,
                             salary=700,
                             birthday=date1)
        employee2 = Employee(username='user2',
                             email='test2@gmail.com',
                             first_name='test_first_name',
                             last_name='test_last_name',
                             password='test1234',
                             department_id=1,
                             salary=500,
                             birthday=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(600, department_service.get_average_salary(department.to_dict()))

    def test_get_average_age(self):
        """
        Testing the average_age by department by adding a new department and employees
        and compares the received value with the given one.
        If they are equal then the test is successful
        """
        department = Department(name='test_department_age', description='test')
        # pylint: disable=no-member
        db.session.add(department)
        date1 = datetime.strptime('10/06/1998', '%m/%d/%Y').date()
        date2 = datetime.strptime('06/10/1991', '%m/%d/%Y').date()
        employee1 = Employee(
            username='user1',
            email='test1@gmail.com',
            first_name='test_first_name',
            last_name='test_last_name',
            password='test1234',
            department_id=1,
            salary=700,
            birthday=date1
        )
        employee2 = Employee(
            username='user2',
            email='test2@gmail.com',
            first_name='test_first_name',
            last_name='test_last_name',
            password='test1234',
            department_id=1,
            salary=500,
            birthday=date2
        )
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(26.0, department_service.get_average_age(department.to_dict()))
