from flask import Flask
from flask_restful import Api

from data import jobs_resources
from data import users_resources
from data.db_session import global_init

app = Flask(__name__)
api = Api(app)

api.add_resource(jobs_resources.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resources.JobsResource, '/api/v2/jobs/<int:jobs_id>')
api.add_resource(users_resources.UsersListResource, '/api/v2/users')
api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:user_id>')

if __name__ == '__main__':
    global_init('db/db.db')
    app.run('127.0.0.1', 4321)
