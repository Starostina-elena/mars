from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    work_size = IntegerField('Кол-во часов работы', validators=[DataRequired()])
    team_leader = IntegerField('ID тимлида')
    collaborators = StringField('ID участников', validators=[DataRequired])
    start_date = DateField('Дата начала работ')
    end_date = DateField('Дата окончания работ')
    is_finished = BooleanField('Работа закончена?')
    submit = SubmitField('Добавить работу')
