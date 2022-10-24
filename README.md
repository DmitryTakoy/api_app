# api_final
**Описание.**

Yatube - это сайт для публикации своих статей, основная задача этого блога, не только информация, это еще и возможность поделиться с друзьями своими знаниями и умениями. 
Данный проект позволяет создавать, редактировать, удалять посты, визуализировать контент изображениями, а также подписываться на интересных авторов, чтобы всегда оставаться в курсе событий. Причем делать всё это по API.

**Используемые технологии**

Django                        2.2.16
django-filter                 2.4.0
djangorestframework           3.12.4
djangorestframework-simplejwt 4.7.2
isort                         5.10.1
Pillow                        8.3.1
pip                           20.1.1
PyJWT                         2.1.0
pytest                        6.2.4
pytest-django                 4.4.0
requests                      2.26.0
sqlparse                      0.4.3
typed-ast                     1.5.4
typing-extensions             4.4.0
urllib3                       1.26.12
wrapt                         1.14.1
zipp                          3.9.0 `
**Установка.**
1. Клонируйте репозиторий с последней версией проекта

`git clone git@github.com:DmitryTakoy/api_final_yatube.git `

2. Установите виртуальное окружение  

`python3 -m venv venv `

3. Установите зависимости 

` pip install -r requirements.txt `

4. Выполните миграции

`  python3 manage.py migrate `

5. Запустите проект на локальной машине 

` python3 manage.py runserver `

**Примеры запросов/ответов.**

[Получение публикаций: запрос/ответ](https://yadi.sk/d/jBnEHvADBSjFWg)

[Подписка на автора: запрос/ответ](https://yadi.sk/d/uuSeeR6gt-oazg)

[Получение токена: запрос/ответ](https://yadi.sk/d/tNlBiWS2tKma9Q)

Подробное описание эндпоинтов и способов взаимодействия доступны по эндпоинту ``http://localhost:8000/api/redoc/`` после запуска проекта.



