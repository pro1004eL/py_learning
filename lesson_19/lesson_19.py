import requests
import json

url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
response = requests.get(url)

# Перевірка статус-коду
# if response.status_code == 200:
#     data = response.json()  # отримання даних у форматі JSON
#     print('Отримано дані:', data)
# else:
#     print('Помилка. Статус-код:', response.status_code)

status_code = response.status_code
text = response.text
headers = dict(response.headers)

response_json = response.json() # == json.loads(response.text)

print('status_code', status_code)
print('text', text)
print('--'*80)
print('headers', headers)
print('--'*80)
print('response_json', response_json)


