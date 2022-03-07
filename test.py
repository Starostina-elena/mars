from requests import get

print(get('http://127.0.0.1:5000/api/jobs').json())  # корректный запрос - все работы
print(get('http://127.0.0.1:5000/api/jobs/1').json())  # корректный запрос - одна работа
print(get('http://127.0.0.1:5000/api/jobs/100').json())  # некорректный запрос - нет такого id
print(get('http://127.0.0.1:5000/api/jobs/aaa').json())  # некорректный запрос - строка вместо id
