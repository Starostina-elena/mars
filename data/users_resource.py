from flask import jsonify
from flask_restful import abort, Api, Resource

from . import db_session
from .users import User
from .user_reqparse import parser


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(User).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class UsersResource(Resource):

    def get(self, user_id):
        abort_if_news_not_found(user_id)

        session = db_session.create_session()
        news = session.query(User).get(user_id)

        return jsonify({'users': news.to_dict()})

    def delete(self, user_id):

        abort_if_news_not_found(user_id)

        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()

        return jsonify({'success': 'OK'})


class UsersListResource(Resource):

    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict() for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()

        user = User(
            id=args['id'],
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email']
        )
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
