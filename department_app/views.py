from department_app.app import app
from flask import render_template
from department_app.models import Department, Employee


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departments')
def departments():
    departs = Department.query.all()
    return render_template('departments.html', departs=departs)


@app.route('/employees')
def employees():
    employees_list = Employee.query.all()
    return render_template('employees.html', employees_list=employees_list)


@app.route('/employees/department/<depart_id>')
def employees_department_list(depart_id):
    print(type(depart_id))
    employees_list = Employee.query.filter_by(department_id=int(depart_id))
    print(employees_list)
    return render_template('employees.html', employees_list=employees_list)


