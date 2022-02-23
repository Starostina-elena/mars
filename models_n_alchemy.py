from flask import Flask, render_template, redirect
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/users_and_jobs.db")
    session = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Colfer"
    user.name = "Christine"
    user.age = 32
    user.position = "captain's assistant"
    user.speciality = "engineer"
    user.address = "module_2"
    user.email = "Chris@mars.org"
    user.hashed_password = "Christine32"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Rassel"
    user.name = "Jack"
    user.age = 26
    user.position = "worker"
    user.speciality = "research engineer"
    user.address = "module_3"
    user.email = "Rassel@mars.org"
    user.hashed_password = "123KHJBKJwkjn67tHGsyuwcjz_!"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Brown"
    user.name = "Alex"
    user.age = 18
    user.position = "worker"
    user.speciality = "research engineer"
    user.address = "module_4"
    user.email = "alex_brown@mars.org"
    user.hashed_password = "alexbrown"
    session.add(user)
    session.commit()
    # app.run()


if __name__ == '__main__':
    main()
