import requests
from requests.auth import HTTPBasicAuth
import time

from query_generate import * 
from graph_create import *

# URL сервера Fuseki
url = 'http://178.154.220.21:3030/test/update'


# Установка заголовков для отправки запроса
headers = {
    'Content-Type': 'application/sparql-update',
    'Accept': 'application/json'
}

# Добавление авторизации
username = 'admin'
password = '123'

# Создание экземпляра класса
generator = DictionaryGenerator()

output_file = 'response_times.txt'  # Имя файла для записи времени ответов

with open(output_file, 'w') as file:
    for i in range (10000):
        start_time = time.time()  # Фиксация времени начала отправки запроса
        # Отправка POST запроса на сервер Fuseki с авторизацией
        # Параметры запроса
        graph = generator.generate_dictionary()
        # SPARQL запрос
        query = new_complex_query(graph["id"], graph["history"])
        params = {
            'query': query
        }
        response = requests.post(url, headers=headers,
                                auth=HTTPBasicAuth(username, password),
                                data=query)
        # Проверка статуса ответа
        if response.status_code == 204:
            end_time = time.time()  # Фиксация времени получения ответа
            print(f'{i} Данные успешно записаны на сервер Fuseki ({end_time - start_time})')
        else:
            print('Ошибка при записи данных на сервер Fuseki:', response.text)
        
        file.write(f'{i+1}: {end_time - start_time}\n')