"""
This module consists of the CRUD operations to work with `departments` table
"""
# pylint: disable=cyclic-import
from department_app import db

# pylint: disable=relative-beyond-top-level
from ..models.department import Department
from ..models.employee import Employee


def get_all_departments():
    """
    Select all records from departments table
    :return: the list of all departments in json format
    """
    departments = Department.query.all()
    return [department.to_dict() for department in departments]


def add_department(name, description):
    """
    Add a new department to departments table
    :param name: the department name
    :param description: the department description
    """
    department = Department(name=name, description=description)
    # pylint: disable=no-member
    db.session.add(department)
    db.session.commit()


# pylint: disable=invalid-name
def update_department(id, name, description):
    """
    Update an existing department
    :param id: id by which the required department is updated
    :param name: the department name
    :param description: the department description
    """
    department = Department.query.get_or_404(id)
    department.name = name
    department.description = description
    # pylint: disable=no-member
    db.session.add(department)
    db.session.commit()


# pylint: disable=invalid-name
def update_department_patch(id, name, description):
    """
    Update an existing department without overwriting the unspecified elements with null
    :param id: id by which the required department is updated
    :param name: the department name
    :param description: the department description
    """
    department = Department.query.get_or_404(id)
    if name:
        department.name = name
    elif description:
        department.description = description
    # pylint: disable=no-member
    db.session.add(department)
    db.session.commit()


# pylint: disable=invalid-name
def delete_department(id):
    """
    Delete an existing department
    :param id: id by which the required department is deleted
    """
    department = Department.query.get_or_404(id)
    # pylint: disable=no-member
    db.session.delete(department)
    db.session.commit()


# pylint: disable=invalid-name
def get_department_by_id(id):
    """
    Get a specific department from departments table by id
    :param id: id by which the required department is taken
    :return: the department with a special id
    """
    department = Department.query.get(id)
    return department.to_dict()


def get_average_salary(department):
    """
    Get an average salary of all employees in department
    :return: the average salary of all employees in department
    """
    employees = Employee.query.filter_by(department_id=department['id']).all()
    average_salary = 0

    for employee in employees:
        average_salary += employee.salary

    if len(employees) > 0:
        average_salary /= len(employees)

    return round(average_salary, 2)


def get_average_age(department):
    """
    Get an average age of all employees in department
    :return: the average age of all employees in department
    """
    employees = Employee.query.filter_by(department_id=department['id']).all()
    average_age = 0

    for employee in employees:
        average_age += employee.calculate_age(employee.birthday)

    if len(employees) > 0:
        average_age /= len(employees)

    return round(average_age, 1)
