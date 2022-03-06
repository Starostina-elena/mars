from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from forms.user import RegisterForm, LoginForm
from forms.job import AddJob
from data.users import User
from data.jobs import Jobs
from data import db_session

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/")
def index():
    db_sess = db_session.create_session()

    data = []
    for i in db_sess.query(Jobs):
        teamlead = db_sess.query(User).filter(User.id == i.team_leader)[0]
        to_add_to_data = {
            'id': i.id,
            'title': i.job,
            'team_leader': teamlead.name + ' ' + teamlead.surname,
            'duration': i.work_size,
            'collaborators': i.collaborators,
            'finished': i.is_finished
        }
        data.append(to_add_to_data)

    return render_template('works_log.html', title='Works Log', data=data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            email=form.email.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
@login_required
def add_job():
    form = AddJob()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            job=form.title.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            is_finished=form.is_finished.data,
            team_leader=form.team_leader.data,
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Добавить работу', form=form)


def main():
    db_session.global_init("db/users_and_jobs.db")
    app.run()


if __name__ == '__main__':
    main()
