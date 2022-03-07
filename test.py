from requests import put, get

print(put('http://127.0.0.1:5000/api/jobs/1',
          json={'id': 4,
                'job': 'Building main house222',
                'work_size': 20,
                'collaborators': '3, 4',
                'start_date': None,
                'end_date': None,
                'is_finished': False,
                'team_leader': 1,
                'creator': 5}).json())  # корректный запрос

print(put('http://127.0.0.1:5000/api/jobs/10000',
          json={'id': 4,
                'job': 'Building main house222',
                'work_size': 20,
                'collaborators': '3, 4',
                'start_date': None,
                'end_date': None,
                'is_finished': False,
                'team_leader': 1,
                'creator': 5}).json())  # некорректный запрос - нет такого id

print(put('http://127.0.0.1:5000/api/jobs/aaa',
          json={'id': 4,
                'job': 'Building main house222',
                'work_size': 20,
                'collaborators': '3, 4',
                'start_date': None,
                'end_date': None,
                'is_finished': False,
                'team_leader': 1,
                'creator': 5}).json())  # некорректный запрос - id не число

print(get('http://127.0.0.1:5000/api/jobs').json())
