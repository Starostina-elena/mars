import datetime

from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.department import Department


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/users_and_jobs.db")
    session = db_session.create_session()

    first_dep_collaborators = session.query(Department).filter(Department.id == 1).first().members.split(', ')
    first_dep_collaborators = list(map(int, first_dep_collaborators))

    all_collaborators = dict()
    for i in session.query(Jobs).filter(Jobs.is_finished).all():
        collaborators = list(map(int, i.collaborators.split(', ')))
        for j in collaborators:
            if j in all_collaborators:
                all_collaborators[j] += i.work_size
            else:
                all_collaborators[j] = i.work_size

    for i in first_dep_collaborators:
        if i in all_collaborators and all_collaborators[i] > 25:
            worker = session.query(User).filter(User.id == i).first()
            print(worker.surname, worker.name)

    # app.run()


if __name__ == '__main__':
    main()
