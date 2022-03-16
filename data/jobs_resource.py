from flask import jsonify
from flask_restful import abort, Api, Resource

from . import db_session
from .jobs import Jobs
from .job_reqparse import parser


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):

    def get(self, job_id):
        abort_if_job_not_found(job_id)

        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)

        return jsonify({'jobs': job.to_dict()})

    def delete(self, job_id):

        abort_if_job_not_found(job_id)

        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()

        return jsonify({'success': 'OK'})


class JobsListResource(Resource):

    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict() for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()

        job = Jobs(
            id=args['id'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished=args['is_finished'],
            team_leader=args['team_leader']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
