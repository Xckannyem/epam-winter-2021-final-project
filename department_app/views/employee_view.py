from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required

from .. import db
from ..models.employee import Employee
from ..forms import EmployeeAssignForm, EmployeeForm

from . import user


@user.route('/employees')
@login_required
def show_employees():
    """
    Show all employees
    """
    employees = Employee.query.all()

    return render_template('employees/employees.html', employees=employees)


@user.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a department to an employee
    """
    employee_to_assign = Employee.query.get_or_404(id)

    form = EmployeeAssignForm(obj=employee_to_assign)
    if form.validate_on_submit():
        employee_to_assign.department = form.department.data
        db.session.add(employee_to_assign)
        db.session.commit()
        flash('You have successfully assigned a department.', category='success')

        # redirect to the roles page
        return redirect(url_for('user.show_employees'))

    return render_template('employees/assign_employee.html',
                           employee=employee_to_assign, form=form)


@user.route('/employees/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_employee(id):
    """
    Edit an employee
    """
    add_emp = False

    employee = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=employee)
    if form.validate_on_submit():
        employee.first_name = form.first_name.data
        employee.last_name = form.last_name.data
        employee.salary = form.salary.data
        employee.birthday = form.birthday.data
        db.session.commit()
        flash('You have successfully edited the employee.', category='success')

        # redirect to the departments page
        return redirect(url_for('user.show_employees'))

    form.first_name.data = employee.first_name
    form.last_name.data = employee.last_name
    form.salary.data = employee.salary
    form.birthday.data = employee.birthday
    return render_template('employees/edit_employee.html', action="Edit",
                           add_emp=add_emp, form=form,
                           employee=employee)


@user.route('/employees/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash('You have successfully deleted the employee.', category='success')

    # redirect to the departments page
    return redirect(url_for('user.show_departments'))
