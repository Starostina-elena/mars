from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired, Optional


class AddJob(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    work_size = IntegerField('Кол-во часов работы', validators=[DataRequired()])
    team_leader = IntegerField('ID тимлида')
    collaborators = StringField('ID участников')
    start_date = DateField('Дата начала работ', validators=[Optional()])
    end_date = DateField('Дата окончания работ', validators=[Optional()])
    is_finished = BooleanField('Работа закончена?')
    submit = SubmitField('Добавить работу')
