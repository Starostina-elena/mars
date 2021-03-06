import datetime
import os
from json import loads

from flask import Flask, render_template, redirect, request, abort, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from flask_restful import reqparse, abort, Api, Resource

from forms.user import RegisterForm, LoginForm
from forms.job import AddJob
from forms.form_department import AddDepartment

from data.users import User
from data.jobs import Jobs
from data.category import Category
from data.department import Department

from data import db_session, jobs_api, users_api

from Samples_yandex_maps_api import geocoder

from requests import get


app = Flask(__name__)
api = Api(app, catch_all_404s=True)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


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
            'finished': i.is_finished,
            'creator': i.creator
        }
        data.append(to_add_to_data)

    return render_template('works_log.html', title='Works Log', data=data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='??????????????????????', form=form,
                                   message="?????????? ???????????????????????? ?????? ????????")
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
    return render_template('register.html', title='??????????????????????', form=form)


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
                               message="???????????????????????? ?????????? ?????? ????????????",
                               form=form)
    return render_template('login.html', title='??????????????????????', form=form)


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
            creator=current_user.id
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='???????????????? ????????????', second_title='Adding a job', form=form)


@app.route('/editjob/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    form = AddJob()
    if request.method == "GET":
        db_sess = db_session.create_session()
        if current_user.id == 1:
            job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        else:
            job = db_sess.query(Jobs).filter(Jobs.id == job_id, Jobs.creator == current_user.id).first()
        if job:
            form.title.data = job.job
            form.work_size.data = job.work_size
            form.team_leader.data = job.team_leader
            form.collaborators.data = job.collaborators
            form.start_date.data = job.start_date
            form.end_date.data = job.end_date
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if current_user.id == 1:
            job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        else:
            job = db_sess.query(Jobs).filter(Jobs.id == job_id, Jobs.creator == current_user.id).first()
        if job:
            job.job = form.title.data
            job.work_size = form.work_size.data
            job.team_leader = form.team_leader.data
            job.collaborators = form.collaborators.data
            job.start_date = form.start_date.data
            job.end_date = form.end_date.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_job.html', title='???????????????????????????? ????????????', second_title='Edit job', form=form)


@app.route('/deletejob/<int:job_id>', methods=['GET', 'POST'])
@login_required
def news_delete(job_id):
    db_sess = db_session.create_session()
    if current_user.id == 1:
        job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    else:
        job = db_sess.query(Jobs).filter(Jobs.id == job_id, Jobs.creator == current_user.id).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/departments')
def show_departments():
    db_sess = db_session.create_session()

    data = []
    for i in db_sess.query(Department):
        to_add_to_data = {
            'id': i.id,
            'title': i.title,
            'chief_name': i.chief_user.name + ' ' + i.chief_user.surname,
            'chief_id': i.chief_user.id,
            'members': i.members,
            'email': i.email,
        }
        data.append(to_add_to_data)

    return render_template('show_departments.html', title='List of departments', data=data)


@app.route('/adddepartment', methods=['GET', 'POST'])
@login_required
def add_department():
    form = AddDepartment()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dep = Department(
            title=form.title.data,
            chief=form.chief.data,
            members=form.members.data,
            email=form.email.data
        )
        db_sess.add(dep)
        db_sess.commit()
        return redirect('/departments')
    return render_template('add_department.html', title='???????????????? ??????????????????????', second_title='Adding a department', form=form)


@app.route('/editdepartment/<int:dep_id>', methods=['GET', 'POST'])
def edit_department(dep_id):
    form = AddDepartment()
    if request.method == "GET":
        db_sess = db_session.create_session()
        if current_user.id == 1:
            dep = db_sess.query(Department).filter(Department.id == dep_id).first()
        else:
            dep = db_sess.query(Department).filter(Department.id == dep_id, Department.chief == current_user.id).first()
        if dep:
            form.title.data = dep.title
            form.chief.data = dep.chief
            form.members.data = dep.members
            form.email.data = dep.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if current_user.id == 1:
            dep = db_sess.query(Department).filter(Department.id == dep_id).first()
        else:
            dep = db_sess.query(Department).filter(Department.id == dep_id, Department.chief == current_user.id).first()
        if dep:
            dep.title = form.title.data
            dep.chief = form.chief.data
            dep.members = form.members.data
            dep.email = form.email.data
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('add_department.html', title='???????????????????????????? ????????????????????????', second_title='Edit job', form=form)


@app.route('/deletedepartment/<int:dep_id>')
def delete_department(dep_id):
    db_sess = db_session.create_session()
    if current_user.id == 1:
        dep = db_sess.query(Department).filter(Department.id == dep_id).first()
    else:
        dep = db_sess.query(Department).filter(Department.id == dep_id, Department.chief == current_user.id).first()
    if dep:
        db_sess.delete(dep)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


@app.route('/users_show/<int:user_id>')
def nostalgia(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    if user:
        user = get(f'http://localhost:5000/api/users/{user_id}').json()
        ll, spn = geocoder.get_ll_span(user['users']['city_from'])  # ??????????
        return render_template('nostalgia.html', title='????????????????????',
                               name=user['users']['name'] + ' ' + user['users']['surname'],
                               city=user['users']['city_from'],
                               yandex_maps_request=f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l=sat")
    else:
        return render_template('message.html', title='????????????', message='?????? ???????????? id')


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if request.method == "GET":
        return render_template('carousel.html', title='?????????????? ??????????????', number_pics=len(os.listdir('static\\img\\mars_carousel')))
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static\\img\\mars_carousel\\mars_carousel_{len(os.listdir("static/img/mars_carousel")) + 1}.jpg', mode='wb') as file:
            file.write(f.read())
        return render_template('carousel.html', title='?????????????? ??????????????',
                               number_pics=len(os.listdir('static\\img\\mars_carousel')))


@app.route('/member')
def member():
    with open('templates/user_info.json', encoding='utf-8') as file:
        json_file = loads(file.read())
    return render_template('member.html', title='Member', json_file=json_file)


def main():
    db_session.global_init("db/users_and_jobs.db")
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
