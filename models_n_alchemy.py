import datetime

from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/users_and_jobs.db")
    session = db_session.create_session()

    for i in session.query(User).filter(User.address == 'module_1', User.speciality.notlike('%engineer%'),
                                        User.position.notlike('%engineer%')):
        print(i.id)

    # app.run()


if __name__ == '__main__':
    main()
