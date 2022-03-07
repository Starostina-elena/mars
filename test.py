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
                 'creator': 5}).json())
