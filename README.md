
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://pypi.org/project/SQLAlchemy/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=043A6B)](https://pypi.org/project/alembic/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://pypi.org/project/pydantic/)
[![Asyncio](https://img.shields.io/badge/-Asyncio-464646?style=flat&logo=Asyncio&logoColor=ffffff&color=043A6B)](https://docs.python.org/3/library/asyncio.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
# Test_task-1_Bewise
Тестовое задание №1 Bewise.ai


Задание:   
1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.  

2. Реализовать на Python3 веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:  
    - В сервисе должно быть реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.
    - После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
    - Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
    - Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.
3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.
4. Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAalchemy,  пользоваться аннотацией типов.

### Запуск проекта
1. Скачать и установить [Docker](https://docs.docker.com/get-docker/)
2. Клонировать репозиторий ```git clone git@github.com:Hastred45/bewise_task_1.git``` 
3. В корне директории bewise_task_1 создать файл .env и заполнить его по примеру .env.example
4. В папке infra выполнить команду ```docker compose up -d```
5. Перейти по адресу ```http://127.0.0.1:8000/docs```

### Примеры запросов

1. Запрос количества вопросов в БД  
_**GET .../question/**_
```JSON
{
  "quantity": "int"
}
```
![1](https://raw.github.com/Hastred45/bewise_task_1/f8ec7c9d36657da1364b4369f8ca541df315a35c/Screenshot_2.png)  
  
  
2. Запрос на получение вопросов от API jservice.io  
_**POST.../question/?quest_num=1**_
```JSON
{
  "question": "str",
  "answer": "str"
}
```
![1](https://raw.github.com/Hastred45/bewise_task_1/f8ec7c9d36657da1364b4369f8ca541df315a35c/Screenshot_3.png)  
  
  
Запрос на получение вопросов из БД  
_**GET.../question/?quest_num=1**_
```JSON
{
  "question": "str",
  "answer": "str"
}
```
![1](https://raw.github.com/Hastred45/bewise_task_1/f8ec7c9d36657da1364b4369f8ca541df315a35c/Screenshot_4.png)
