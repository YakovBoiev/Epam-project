from flask import jsonify, request
from department_app.app import app, db
from department_app.models import Department, Employee


def depart_to_dict(department):
    return {
        'id': department.id,
        'names': department.names,
        'number_employees': department.number_employees,
        'average_salary': department.average_salary
    }


def employee_to_dict(employee):
    return {
        'id': employee.id,
        'tax_number': employee.tax_number,
        'last_name': employee.last_name,
        'first_name': employee.first_name,
        'date_of_birth': employee.date_of_birth,
        'salary': employee.salary,
        'department_id': employee.department_id,
        'departament_name': employee.department.names
    }


@app.route('/api/department/', methods=["POST"])
def department_create_api():
    names = request.json.get('names', '')
    if not names:
        return jsonify({"error": "Incorrect request"}), 400
    department = Department(names=names)
    db.session.add(department)
    db.session.commit()
    return jsonify(depart_to_dict(department))


@app.route('/api/department/', methods=["GET"])
def departments_api():
    department_list = Department.query.order_by(Department.id).all()
    return jsonify([depart_to_dict(department) for department in department_list])


@app.route('/api/department/<int:id_>', methods=["GET"])
def department_read_api(id_):
    department = Department.query.get(id_)
    if department is None:
        return jsonify({"error": "Department not found"}), 404
    return jsonify(depart_to_dict(department))


@app.route('/api/department/<int:id_>', methods=["PUT"])
def department_update_api(id_):
    department = Department.query.get(id_)
    if department is None:
        return jsonify({"error": "Department not found"}), 404
    names = department.names
    names = request.json.get('names', names)
    department.names = names
    db.session.commit()
    return jsonify(depart_to_dict(department))


@app.route('/api/department/<int:id_>', methods=["DELETE"])
def department_delete_api(id_):
    department = Department.query.get(id_)
    if not department:
        return jsonify({"error": "Department not found"}), 404
    db.session.delete(department)
    db.session.commit()
    return "", 204


@app.route('/api/employee/', methods=["POST"])
def employee_create_api():
    employee_data = request.json
    employee = Employee(**employee_data)  # need validate
    db.session.add(employee)
    db.session.commit()
    return jsonify(employee_to_dict(employee))


@app.route('/api/employee/', methods=["GET"])
def employees_api():
    employee_list = Employee.query.order_by(Employee.id).all()
    return jsonify([employee_to_dict(employee) for employee in employee_list])


@app.route('/api/employee/<int:id_>', methods=["GET"])
def employee_read_api(id_):
    employee = Employee.query.get(id_)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(employee_to_dict(employee))


@app.route('/api/employee/<int:id_>', methods=["PUT"])
def employee_update_api(id_):
    employee = Employee.query.get(id_)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404
    employee.tax_number = request.json.get('tax_number', employee.tax_number)
    employee.last_name = request.json.get('last_name', employee.last_name)
    employee.first_name= request.json.get('first_name', employee.first_name)
    employee.date_of_birth = request.json.get('date_of_birth', employee.date_of_birth)
    employee.salary = request.json.get('salary', employee.salary)
    employee.department_id= request.json.get('department_id', employee.department_id)
    db.session.commit()
    return jsonify(employee_to_dict(employee))


@app.route('/api/employee/<int:id_>', methods=["DELETE"])
def employee_delete_api(id_):
    employee = Employee.query.get(id_)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(employee)
    db.session.commit()
    return "", 204
