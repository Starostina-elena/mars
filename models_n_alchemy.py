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

    jobs = session.query(Jobs).all()

    team_leaders = []
    max_len_team = 0

    for i in jobs:
        if len(i.collaborators.split(', ')) == max_len_team:
            team_leaders.append(i.team_leader)
        elif len(i.collaborators.split(', ')) > max_len_team:
            team_leaders = [i.team_leader]
            max_len_team = len(i.collaborators.split(', '))

    for i in team_leaders:
        team_lead = session.query(User).filter(User.id == i)[0]
        print(team_lead.name, team_lead.surname)

    # app.run()


if __name__ == '__main__':
    main()
