from department_app.app import app
from flask import render_template
from department_app.models import Department


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departments')
def departments():
    departs = Department.query.all()
    print(departs[0].names)
    return render_template('departments.html', departs=departs)


@app.route('/employees')
def employees():
    return render_template('employees.html')
