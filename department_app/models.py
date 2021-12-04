from department_app.app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(80), unique=True, nullable=True)