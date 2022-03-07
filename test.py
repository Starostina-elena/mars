from requests import get, post

print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 100,
                 'job': 'Building main house',
                 'work_size': 30,
                 'collaborators': '3, 4',
                 'start_date': None,
                 'end_date': None,
                 'is_finished': True,
                 'team_leader': 1,
                 'creator': 5}).json())  # корректный запрос

print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 1,
                 'job': 'Building main house',
                 'work_size': 30,
                 'collaborators': '3, 4',
                 'start_date': None,
                 'end_date': None,
                 'is_finished': True,
                 'team_leader': 1,
                 'creator': 5}).json())  # такой id уже есть

print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 200,
                 'job': 'Building main house',
                 'work_size': 30,
                 'collaborators': '3, 4',
                 'is_finished': True,
                 'team_leader': 1,
                 'creator': 5}).json())  # не хватает параметров start_date и end_date

print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 300,
                 'job': 'Building main house',
                 'work_size': 30,
                 'collaborators': '3, 4',
                 'start_date': None,
                 'end_date': None,
                 'is_finished': True,
                 'team_leader': 100,
                 'creator': 5}).json())  # нет пользователя с таким id, как у тимлида

print(get('http://127.0.0.1:5000/api/jobs').json())
