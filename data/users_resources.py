from flask import jsonify, abort, request
from flask_restful import Resource, reqparse

from data.db_session import create_session
from data.users import User

parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('city', required=True)


def abort_if_user_not_found(user_id):
    session = create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404)


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = create_session()
        user = db_sess.query(User).filter(User.id == user_id).first()
        return jsonify(
            {
                'user': user.to_dict(),
                'status': 200
            }
        )

    def put(self, user_id):
        if not request.json:
            abort(400)
        try:
            args = parser.parse_args(strict=True)
        except ValueError:
            abort(400)
        abort_if_user_not_found(user_id)
        db_sess = create_session()
        user = db_sess.query(User).filter(User.id == user_id).first()
        db_sess.delete(user)
        user.surname = args.surname
        user.name = args.name
        user.age = args.age
        user.position = args.position
        user.speciality = args.speciality
        user.address = args.address
        user.email = args.email
        user.city = args.city
        db_sess.add(user)
        db_sess.commit()
        return jsonify(
            {
                'edited_user': user.to_dict()
            }
        )

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        db_sess = create_session()
        users = db_sess.query(User).all()
        return jsonify(
            {
                'users':
                    [item.to_dict()
                     for item in users],
                'status': 200
            }
        )

    def post(self):
        try:
            args = parser.parse_args()
        except ValueError:
            return jsonify(
                {
                    'error': 'Bad request'
                }
            )
        session = create_session()
        user = User()
        user.surname = args.surname
        user.name = args.name
        user.age = args.age
        user.position = args.position
        user.speciality = args.speciality
        user.address = args.address
        user.email = args.email
        user.city = args.city
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
