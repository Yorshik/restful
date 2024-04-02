from flask import abort, jsonify, request
from flask_restful import Resource, reqparse

from data.db_session import create_session
from data.jobs import Jobs

parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True)
parser.add_argument('job', required=True)
parser.add_argument('is_finished', required=True, type=bool)
parser.add_argument('collaborators', required=True)
parser.add_argument('work_size', required=True, type=int)


def abort_if_jobs_not_found(jobs_id):
    session = create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404)


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify(
            {
                'jobs': jobs.to_dict(
                    only=('team_leader', 'job', 'collaborators', 'is_finished', 'work_size')
                )
            }
        )

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, jobs_id):
        print('ХУУУУУУЙ')
        if not request.json:
            print('BLYAAAD')
            return jsonify({'error': 'Empty request'}), 400
        try:
            print('EBAAAAAAAAAAAAT')
            args = parser.parse_args(strict=True)
        except ValueError:
            print('SUKAAAAAAAAAAAAAAAAA')
            return jsonify({'error': 'Bad Request'}), 400
        print('TVOY ROT')
        db_sess = create_session()
        abort_if_jobs_not_found(jobs_id)
        print('IVANZOLO')
        job = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
        db_sess.delete(job)
        job.team_leader = args.team_leader
        job.job = args.job
        job.work_size = args.work_size
        job.collaborators = args.collaborators
        job.is_finished = args.is_finished
        db_sess.add(job)
        db_sess.commit()
        print('SASAT')
        return jsonify(
            {
                'edited_job': job.to_dict()
            }
        )


class JobsListResource(Resource):
    def get(self):
        session = create_session()
        jobs = session.query(Jobs).all()
        return jsonify(
            {
                'jobs': [item.to_dict(
                    only=('team_leader', 'job', 'collaborators', 'is_finished', 'work_size')
                ) for item in jobs]
            }
        )

    def post(self):
        print()
        try:
            args = parser.parse_args()
        except ValueError:
            print(1)
            return abort(400)
        session = create_session()
        jobs = Jobs()
        jobs.team_leader = args.team_leader
        jobs.job = args.job
        jobs.collaborators = args.collaborators
        jobs.is_finished = args.is_finished
        jobs.work_size = args.work_size
        session.add(jobs)
        session.commit()
        return jsonify({'id': jobs.id})
