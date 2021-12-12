from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired


class DepartmentForm(FlaskForm):
    names = StringField('Department name', validators=[DataRequired(), Length(max=80)])
    submit = SubmitField('Send')

