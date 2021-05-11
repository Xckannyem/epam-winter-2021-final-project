from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from .. import db
from ..models.department import Department
from ..forms import DepartmentForm

from . import user


@user.route('/departments', methods=['GET', 'POST'])
@login_required
def show_departments():
    """
    Show all departments
    """
    departments = Department.query.all()

    return render_template('departments/departments.html', departments=departments)


@user.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    add_dep = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department_to_create = Department(
            name=form.name.data,
            description=form.description.data
        )
        try:
            # add department to the database
            db.session.add(department_to_create)
            db.session.commit()
            flash('You have successfully added a new department.', category='success')
        except:
            # in case department already exists
            flash('Department already exists!', category='danger')

        # redirect to department page
        return redirect(url_for('user.show_departments'))

    # load department template
    return render_template('departments/department.html', action='Add',
                           add_dep=add_dep, form=form)


@user.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    add_dep = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.', category='success')

        # redirect to the departments page
        return redirect(url_for('user.show_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('departments/department.html', action="Edit",
                           add_dep=add_dep, form=form,
                           department=department)


@user.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.', category='success')

    # redirect to the departments page
    return redirect(url_for('user.show_departments'))
