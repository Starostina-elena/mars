from requests import delete, get

print(delete('http://127.0.0.1:5000/api/jobs/1').json())  # корректный запрос
print(delete('http://127.0.0.1:5000/api/jobs/1000').json())  # некорректный запрос - нет такого id
print(delete('http://127.0.0.1:5000/api/jobs/aaa').json())  # некорректный запрос - id строка

print(get('http://127.0.0.1:5000/api/jobs').json())
