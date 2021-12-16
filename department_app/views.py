from department_app.app import app, db
from flask import render_template, redirect, request, url_for
from department_app.forms import DepartmentForm, EmployeeForm
from department_app.models import Department, Employee


@app.route('/index')
@app.route('/')
def index():
    title = 'Main'
    return render_template('index.html', title=title)


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


@app.route('/employee/create', methods=['GET', 'POST'])
def employee_create():
    title = 'Create employee'
    form = EmployeeForm()
    departments_list = []
    for department in Department.query.all():
        departments_list.append((department.id, department.names))
    form.department_id.choices = departments_list
    if form.validate_on_submit():
        employee = Employee(department_id=form.department_id.data,
                            tax_number=form.tax_number.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            date_of_birth=form.date_of_birth.data,
                            salary=form.salary.data)
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('employees_department_list', department_id=employee.department_id))
    return render_template('employee_create.html', form=form, title=title)


@app.route('/employee/<int:_id>')
def employee_read(_id):
    employee = Employee.query.get(_id)
    return render_template('employee_card.html', employee=employee)


@app.route('/employee/update/<int:_id>', methods=['GET', 'POST'])
def employee_update(_id):
    title = "Update employee"
    employee = Employee.query.get(_id)
    form = EmployeeForm()
    departments_list = []
    for department in Department.query.all():
        departments_list.append((department.id, department.names))
    form.department_id.choices = departments_list
    if request.method == 'GET':
        form.tax_number.data = employee.tax_number
        form.first_name.data = employee.first_name
        form.last_name.data = employee.last_name
        form.date_of_birth.data = employee.date_of_birth
        form.salary.data = employee.salary
        return render_template('employee_create.html', form=form, title=title)
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.department_id.data)
            employee.department_id = form.department_id.data,
            employee.tax_number = form.tax_number.data,
            employee.first_name = form.first_name.data,
            employee.last_name = form.last_name.data,
            employee.date_of_birth = form.date_of_birth.data,
            employee.salary = form.salary.data
            db.session.commit()
            return redirect(url_for('employee_read', _id=employee.id))


@app.route('/employee/delete/<int:_id>')
def employee_delete(_id):
    employee = Employee.query.get(_id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('employees'))
