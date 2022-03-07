from requests import delete

print(delete('http://127.0.0.1:5000/api/jobs/100').json())
