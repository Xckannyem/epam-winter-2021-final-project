from datetime import datetime

from department_app import db
from ..models.employee import Employee


def get_all_employees():
    """
    This function is used to select all records from employees table
    :return: the list of all employees
    """
    employees = Employee.query.all()
    return [employee.to_dict() for employee in employees]


def get_employee_by_id(id):
    """
    This function is used to get the single employee by id
    :param id: the id of the employee to get
    :return: the employee with the specified id
    """
    employee = Employee.query.get(id)
    return employee.to_dict()


def add_employee(first_name, last_name, salary, birthday):
    birthday = datetime.strptime(birthday, '%m/%d/%Y')
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        salary=salary,
        birthday=birthday
    )
    db.session.add(employee)
    db.session.commit()


def update_employee(id, first_name, last_name, salary, birthday):
    """
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
    db.session.add(employee)
    db.session.commit()


def delete_employee(id):
    """
    Delete an existing department employee
    :param id: id by which the required employee is deleted
    """
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
