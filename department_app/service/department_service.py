from department_app import db

from ..models.department import Department


def get_all_departments():
    """
    Select all records from departments table
    :return: the list of all departments in json format
    """
    departments = Department.query.all()
    return [department.to_dict() for department in departments]


def get_department_by_id(id):
    """
    Get a specific department from departments table by id
    :param id: id by which the required department is taken
    :return: the department with a special id
    """
    department = Department.query.get(id)
    return department.to_dict()


def add_department(name, description):
    """
    Add a new department to departments table
    :param name: the department name
    :param description: the department description
    """
    department = Department(name=name, description=description)
    db.session.add(department)
    db.session.commit()


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
    db.session.add(department)
    db.session.commit()


def delete_department(id):
    """
    Delete an existing department
    :param id: id by which the required department is deleted
    """
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
