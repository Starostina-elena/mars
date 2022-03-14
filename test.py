from requests import post, get, delete

print(post('http://127.0.0.1:5000/api/v2/users',
           json={'id': 6,
                 'surname': 'awf',
                 'name': 'skbv',
                 'age': 34,
                 'position': None,
                 'speciality': None,
                 'address': None,
                 'email': '121@mars.org',
                 'password': '12345'}).json())  # корректный запрос

print(delete('http://127.0.0.1:5000/api/v2/users/1').json())  # корректный запрос
print(delete('http://127.0.0.1:5000/api/v2/users/600').json())  # корректный запрос

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/4').json())
print(get('http://localhost:5000/api/v2/users/6').json())
print(get('http://localhost:5000/api/v2/users/q').json())
