import requests

response = requests.get("https://api.github.com")  # Отправляем GET-запрос
print(response.status_code)  # Выводим HTTP-статус ответа
print(response.json())  # Выводим JSON-ответ