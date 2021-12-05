from department_app.app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(80), unique=True, nullable=False)

    @property
    def number_employees(self):
        return len(list(Employee.query.filter_by(department_id=self.id)))

    @property
    def average_salary(self):
        query = Employee.query.filter_by(department_id=self.id)
        return sum(map(lambda employee: employee.salary, query))/self.number_employees


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tax_number = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Numeric, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

