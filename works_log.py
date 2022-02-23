import datetime

from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def create_table():

    global session

    data = []
    for i in session.query(Jobs):
        teamlead = session.query(User).filter(User.id == i.team_leader)[0]
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


def main():

    global session

    db_session.global_init("db/users_and_jobs.db")
    session = db_session.create_session()

    app.run()


if __name__ == '__main__':
    main()
