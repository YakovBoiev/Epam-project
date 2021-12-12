from department_app.app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(80), unique=True, nullable=False)
    employees = db.relationship('Employee', backref='department', lazy=True)

    @property
    def number_employees(self):
        return len(self.employees)

    @property
    def average_salary(self):
        try:
            return sum(map(lambda employee: employee.salary, self.employees)) / self.number_employees
        except ZeroDivisionError:
            return 0


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tax_number = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Numeric, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

