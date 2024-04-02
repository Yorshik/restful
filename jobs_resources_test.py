from requests import get, post, put, delete

default = 'http://127.0.0.1:4321'

# /api/v2/jobs GET
print(get(f'{default}/api/v2/jobs'))

# /api/v2/jobs POST
print(post(f'{default}/api/v2/jobs', json={}))
print(
    post(
        f'{default}/api/v2/jobs', json={
            'team_leader': 1,
            'job': 'testing jobs resources',
            'collaborators': '1000, -7',
            'is_finished': False,
            'work_size': 993
        }
        )
    )

# /api/v2/jobs/<int:jobs_id> GET
print(get(f'{default}/api/v2/jobs/123'))
print(get(f'{default}/api/v2/jobs/1'))

# /api/v2/jobs/<int:jobs_id> PUT
print(put(f'{default}/api/v2/jobs/1', json={}))
print(
    put(
        f'{default}/api/v2/jobs/1', json={
            'team_leader': 1,
            'job': 'testing jobs & users resources',
            'collaborators': '1, 2, 3, 993',
            'is_finished': True,
            'work_size': 993 - 7
        }
        )
    )

# /api/v2/jobs/<int:jobs_id> DELETE
print(delete(f'{default}/api/v2/jobs/1234'))
print(delete(f'{default}/api/v2/jobs/1'))
