import flask
from flask import request

from . import db_session
from .jobs import Jobs
from .users import User


blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict() for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'jobs': job.to_dict()
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader', 'creator']):
        return flask.jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    is_teamlead_exist = db_sess.query(User).filter(User.id == request.json['team_leader']).first()
    if not is_teamlead_exist:
        return flask.jsonify({'error': 'Team leader does not exist'})
    is_creator_exist = db_sess.query(User).filter(User.id == request.json['creator']).first()
    if not is_creator_exist:
        return flask.jsonify({'error': 'Creator does not exist'})
    job = Jobs(
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date'],
        is_finished=request.json['is_finished'],
        team_leader=request.json['team_leader'],
        creator=request.json['creator']
    )
    if 'id' in request.json:
        is_id_exists = db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first()
        if is_id_exists:
            return flask.jsonify({'error': 'Id already exists'})
        else:
            job.id = request.json['id']
    db_sess.add(job)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_news(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(job)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_news(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return flask.jsonify({'error': 'Not found'})
    if 'id' in request.json:
        job.id = request.json['id']
    if 'job' in request.json:
        job.job = request.json['job']
    if 'work_size' in request.json:
        job.work_size = request.json['work_size']
    if 'collaborators' in request.json:
        job.collaborators = request.json['collaborators']
    if 'start_date' in request.json:
        job.start_date = request.json['start_date']
    if 'end_date' in request.json:
        job.end_date = request.json['end_date']
    if 'is_finished' in request.json:
        job.is_finished = request.json['is_finished']
    if 'team_leader' in request.json:
        job.team_leader = request.json['team_leader']
    if 'creator' in request.json:
        job.creator = request.json['creator']
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})
