from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired, Optional


class AddDepartment(FlaskForm):
    title = StringField('Название департамента', validators=[DataRequired()])
    chief = IntegerField('ID тимлида', validators=[DataRequired()])
    members = StringField('ID участников', validators=[DataRequired()])
    email = StringField('Email департамента', validators=[DataRequired()])
    submit = SubmitField('Добавить департамент')
