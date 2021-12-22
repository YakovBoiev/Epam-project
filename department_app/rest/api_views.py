from flask import jsonify, request
from department_app.app import app, db
from department_app.models import Department


def depart_to_dict(department):
    return {
        'id': department.id,
        'names': department.names,
        'number_employees': department.number_employees,
        'average_salary': department.average_salary
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




