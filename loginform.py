from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    astronaut_name = StringField('ID астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_name = StringField('ID капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return 'Форма отправлена'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
