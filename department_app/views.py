from department_app.app import app, db
from flask import render_template, redirect, request, url_for
from department_app.forms import DepartmentForm
from department_app.models import Department, Employee


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departments')
def departments():
    department_list = Department.query.all()
    return render_template('departments.html', department_list=department_list)


@app.route('/department/create', methods=["GET", "POST"])
def department_create():
    title = 'Create department'
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(names=form.names.data)
        db.session.add(department)
        db.session.commit()
        return redirect(url_for('departments'))
    return render_template('department_create.html', form=form, title=title)


@app.route('/department/<int:department_id>')
def department_read(department_id):
    department = Department.query.get(department_id)
    return render_template('department_card.html', department=department)


@app.route('/department/update/<int:department_id>', methods=["GET", "POST"])
def department_update(department_id):
    title = 'Update department'
    department = Department.query.get(department_id)
    form = DepartmentForm()
    if request.method == 'GET':
        form.names.data = department.names
        return render_template('department_create.html', form=form, title=title)
    if request.method == 'POST':
        if form.validate_on_submit():
            department.names = form.names.data
            db.session.commit()
            return redirect(url_for('department_read', department_id=department_id))


@app.route('/department/delete/<int:department_id>')
def department_delete(department_id):
    department = Department.query.get(department_id)
    db.session.delete(department)
    db.session.commit()
    return redirect(url_for('departments'))


@app.route('/employees')
def employees():
    employees_list = Employee.query.all()
    return render_template('employees.html', employees_list=employees_list)


@app.route('/employees/department/<int:department_id>')
def employees_department_list(department_id):
    employees_list = Employee.query.filter_by(department_id=department_id)
    return render_template('employees.html', employees_list=employees_list)


