from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField, SelectField
from wtforms.validators import Length, DataRequired


class DepartmentForm(FlaskForm):
    names = StringField('Department name', validators=[DataRequired(), Length(max=80)])
    submit = SubmitField('Send')


class EmployeeForm(FlaskForm):
    department_id = SelectField('Department', coerce=int)
    tax_number = StringField('Tax number', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired(), Length(max=80)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(max=80)])
    date_of_birth = DateField('Date of birth', validators=[DataRequired()])
    salary = DecimalField('Salary', validators=[DataRequired()])
    submit = SubmitField('Send')


