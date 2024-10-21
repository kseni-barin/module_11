#requests - запросить данные с сайта и вывести их в консоль.
#https://requests.readthedocs.io/en/latest/index.html

import requests

r = requests.get('https://api.github.com/events')
print(r)
# получаем объект класса Response и код 200. Этот код говорит, что ресурс работает и можно с ним
# взаимодействовать, но если код 404 - это означает, что страницы нет.
# увидеть код состояния, который возвращается с сервера:
print(r.status_code)
# получить содержимое запроса в байтах:
print(r.content)
# конвертировать полученную информацию в строку в кодировке UTF-8:
r.encoding = 'utf-8'
print(r.text)
#данные в формате JSON:
print(r.json())

#работа с исключениями, пример:
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        r = requests.get(url)
        r.raise_for_status() #вызвать исключение, если ответ успешен, исключения задействованы не будут
    except HTTPError as http_err:
        print(f'Произошла HTTP ошибка: {http_err}')
    except Exception as err:
        print(f'Произошла ошибка: {err}')
    else:
        print('Success!')

print(r.headers) #Получаем заголовки ответа

#HTTP заголовки играют ключевую роль в регулировании передачи данных веб-запросов.
#Пользовательские заголовки могут включать в себя ключи аутентификации, типы данных или обеспечивать
# соблюдение политики CORS
headers = {
    'Authorization': 'Bearer ВАШ_ТОКЕН',
    'Accept-Language': 'en-US',
    'Content-Type': 'application/json'
}

response = requests.get('https://api.example.com/endpoint', headers=headers)

#Установить таймаут, чтобы задать максимальное время ожидания ответа на запрос
response = requests.get('https://example.com', headers=headers, timeout=5)

#параметр auth для осуществления базовой HTTP-аутентификации:
response = requests.get('https://example.com', auth=('username', 'password'))


#Один из распространенных способов настройки GETзапроса — передача значений через параметры строки запроса в URL.
# Чтобы сделать это с помощью get(), вы передаете данные в params в виде словаря или в виде списка кортежей:
rr = requests.get("https://api.github.com/search/repositories", params = [("q", "language:python"), ("sort", "stars"),
("order", "desc")])
print(rr.json())

#другие популярные методы HTTP включают POST, PUT, DELETE, HEAD, PATCH, и OPTIONS, например:
r1=requests.get("https://httpbin.org/get")
print(r1.json())
r2 = requests.post("https://httpbin.org/post", data={"key": "value"})
print(r2.json())
requests.put("https://httpbin.org/put", data={"key": "value"})
r3 = requests.delete("https://httpbin.org/delete")
print(r3.json())
requests.head("https://httpbin.org/get")
requests.patch("https://httpbin.org/patch", data={"key": "value"})
requests.options("https://httpbin.org/get")

