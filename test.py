from requests import post, get, delete

print(post('http://127.0.0.1:5000/api/v2/jobs',
           json={'id': 6,
                 'job': 'awf',
                 'work_size': 20,
                 'collaborators': '3, 4',
                 'start_date': None,
                 'end_date': None,
                 'is_finished': None,
                 'team_leader': 1}).json())  # корректный запрос

print(delete('http://127.0.0.1:5000/api/v2/jobs/6').json())  # корректный запрос
print(delete('http://127.0.0.1:5000/api/v2/jobs/600').json())  # некорректный запрос

print(get('http://localhost:5000/api/v2/jobs').json())  # корректный запрос
print(get('http://localhost:5000/api/v2/jobs/3').json())  # корректный запрос
print(get('http://localhost:5000/api/v2/jobs/6').json())  # некорректный запрос
print(get('http://localhost:5000/api/v2/jobs/q').json())  # некорректный запрос
