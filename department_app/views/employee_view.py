from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from .. import db
from ..models.employee import Employee
from ..forms import EmployeeAssignForm

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

    return render_template('employees/employee.html',
                           employee=employee_to_assign, form=form)
