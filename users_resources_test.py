from requests import get, post, put, delete

default = 'http://127.0.0.1:4321'

# /api/v2/users GET
print(get(f'{default}/api/v2/users'))

# /api/v2/users POST
print(post(f'{default}/api/v2/users', json={}))
print(
    post(
        f'{default}/api/v2/users', json={
            'name': 'PRIVET',
            'surname': 'HAHAHAHA',
            'age': 1000 - 7,
            'address': 'PODVAL',
            'position': "XZ",
            'speciality': 'DUNNO',
            'city': 'Moscow',
            'email': 'sgkgs123sfljghdj@gfjdg.com'
        }
        )
    )

# /api/v2/users/<int:user_id> GET
print(get(f'{default}/api/v2/users/123'))
print(get(f'{default}/api/v2/users/1'))

# /api/v2/users/<int:user_id> PUT
print(put(f'{default}/api/v2/users/1', json={}))
print(
    put(
        f'{default}/api/v2/users/2', json={
            'name': 'HAHAHAHAHA',
            'surname': 'PRIVET',
            'age': 7 - 1000,
            'address': 'XZ',
            'position': "PODVAL",
            'speciality': 'STILL DUNNO',
            'city': 'Moscow',
            'email': 'sgkgssfsfsdsdsfsdfsdhdsfljghdj@gfjdg.com'
        }
        )
    )

# /api/v2/users/<int:user_id> DELETE
print(delete(f'{default}/api/v2/users/1234'))
print(delete(f'{default}/api/v2/users/2'))
