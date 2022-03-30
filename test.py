from requests import post, get, delete

print(post('http://127.0.0.1:5000/api/users',
           json={'id': 7,
                 'surname': 'awf',
                 'name': '20',
                 'age': 30,
                 'position': None,
                 'speciality': None,
                 'address': None,
                 'email': '1',
                 'password': '123',
                 'modified_date': None}).json())  # корректный запрос

print(delete('http://127.0.0.1:5000/api/users/7').json())  # корректный запрос

print(get('http://localhost:5000/api/users').json())  # корректный запрос
print(get('http://localhost:5000/api/users/3').json())  # корректный запрос
