"""
This module consists of the CRUD operations to work with `employees` table
"""
# pylint: disable=cyclic-import
from datetime import datetime

from department_app import db

# pylint: disable=relative-beyond-top-level
from ..models.employee import Employee


def get_all_employees():
    """
    Get all records from employees table
    :return: the list of all employees
    """
    employees = Employee.query.all()
    return [employee.to_dict() for employee in employees]


def add_employee(first_name, last_name, salary, birthday):
    """
    Add a new employee
    :param first_name: the employee first name
    :param last_name: the employee last name
    :param salary: the employee salary
    :param birthday: the employee birthday in format '%m/%d/%Y'
    """
    birthday = datetime.strptime(birthday, '%m/%d/%Y')
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        salary=salary,
        birthday=birthday
    )
    # pylint: disable=no-member
    db.session.add(employee)
    db.session.commit()


# pylint: disable=invalid-name
def update_employee(id, first_name, last_name, salary, birthday):
    """
    Update an existing employee
    :param id: id by which the required employee is updated
    :param first_name: the employee first name
    :param last_name: the employee last name
    :param salary: the employee salary
    :param birthday: the employee birthday in format '%m/%d/%Y'
    """
    employee = Employee.query.get_or_404(id)
    employee.first_name = first_name
    employee.last_name = last_name
    employee.salary = salary
    employee.birthday = birthday
    # pylint: disable=no-member
    db.session.add(employee)
    db.session.commit()


# pylint: disable=invalid-name
def delete_employee(id):
    """
    Delete an existing employee
    :param id: id by which the required employee is deleted
    """
    employee = Employee.query.get_or_404(id)
    # pylint: disable=no-member
    db.session.delete(employee)
    db.session.commit()


# pylint: disable=invalid-name
def get_employee_by_id(id):
    """
    This function is used to get the single employee by id
    :param id: the id of the employee to get
    :return: the employee with the specified id
    """
    employee = Employee.query.get(id)
    return employee.to_dict()


def get_all_employees_in_department(department):
    """
    Get all employees in specified department
    :return: the list of employees working in the specified department
    """
    employees = Employee.query.filter_by(department_id=department['id']).all()
    return [employee.to_dict() for employee in employees]


def get_employees_born_on(born):
    """
    Get all employees born on a specified date
    :param born: the date to filter with
    :return: the list of employees born on a specified date
    """
    born = datetime.strptime(born, '\'%m/%d/%Y\'').date()
    employees = Employee.query.filter_by(birthday=born)
    return [employee.to_dict() for employee in employees]


def get_employees_born_between(start_date, end_date):
    """
    Get all employees born between specified end and start dates
    :param start_date: the date to start comparison with
    :param end_date: the date to end comparison with
    :return: the list of employees born between start and end dates
    """
    start_date = datetime.strptime(start_date, '\'%m/%d/%Y\'').date()
    end_date = datetime.strptime(end_date, '\'%m/%d/%Y\'').date()
    employees = Employee.query.filter(Employee.birthday.between(start_date, end_date))
    return [employee.to_dict() for employee in employees]
