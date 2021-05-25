"""
This module consists of the REST operations to work with employees
"""
# pylint: disable=cyclic-import
from flask import jsonify, request
from flask_restful import Resource

# pylint: disable=relative-beyond-top-level
from ..service import employee_service


class EmployeeListApi(Resource):
    """
    Class for EmployeesListApi Resource available at '/api/employees' url
    """
    @staticmethod
    def get():
        """
        Called when GET request is sent
        :return: all employees in json format
        """
        return jsonify(employee_service.get_all_employees())

    @staticmethod
    def post():
        """
        Called when POST request is sent
        :return: the 'Employee added' response with status code 201
        """
        employee_json = request.json
        if not employee_json:
            return {'message': 'Wrong data'}, 400
        elif employee_json['first_name'] == '' or \
                employee_json['last_name'] == '' or \
                employee_json['salary'] == '' or \
                employee_json['birthday'] == '':
            return {'message': 'Wrong data'}, 400
        try:
            employee_service.add_employee(
                username=employee_json['username'],
                email=employee_json['email'],
                first_name=employee_json['first_name'],
                last_name=employee_json['last_name'],
                password=employee_json['password'],
                department_id=employee_json['department_id'],
                salary=employee_json['salary'],
                birthday=employee_json['birthday']
            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Employee has been successfully added', 201


# pylint: disable=invalid-name
class Employee(Resource):
    """
    Class for Employee Resource available at /employees/<id> url
    """
    @staticmethod
    def get(id):
        """
        Called when GET request is sent
        :return: the employee with a given id in json format
        """
        return jsonify(employee_service.get_employee_by_id(id))

    @staticmethod
    def put(id):
        """
        Called when PUT request is sent
        :return: the 'Employee has been successfully updated' with status code 200
        """
        employee_json = request.json
        if not employee_json:
            return {'message': 'Wrong data'}, 400
        try:
            employee_service.update_employee(
                id,
                username=employee_json['username'],
                email=employee_json['email'],
                first_name=employee_json['first_name'],
                last_name=employee_json['last_name'],
                password=employee_json['password'],
                department_id=employee_json['department_id'],
                salary=employee_json['salary'],
                birthday=employee_json['birthday']
            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Employee has been successfully updated', 200

    # TODO fix patch
    @staticmethod
    def patch(id):
        """
        Called when PATCH request is sent
        :return: the 'Employee has been successfully updated' with status code 200
        """
        department_json = request.json
        try:
            employee_service.update_employee(
                id,
                username=department_json.get('username'),
                email=department_json.get('email'),
                first_name=department_json.get('first_name'),
                last_name=department_json.get('last_name'),
                password=department_json.get('password'),
                department_id=department_json.get('department_id'),
                salary=department_json.get('salary'),
                birthday=department_json.get('birthday')
            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return "Employee has been successfully updated", 200

    @staticmethod
    def delete(id):
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        employee_service.delete_employee(id)
        return 'Employee deleted', 200
