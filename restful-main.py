from flask import Flask, make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource

from data import db_session, users_resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api = Api(app, catch_all_404s=True)


def main():
    db_session.global_init("db/users_and_jobs.db")

    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')

    app.run()


if __name__ == '__main__':
    main()
