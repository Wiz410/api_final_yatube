# api_final
**Api final** это учебный проект 11 спринта в **yandex practicum**.

В нем вы можете через запросы к api:
- Просматривать: посты, комментарии, группы и подписки пользователя.
- Создавать, редактировать и удалять свои посты.
- Создавать, редактировать и удалять комментарии к поста.
- Подписаться на пользователей.

### Требование

- [Python 3.9.10](https://docs.python.org/release/3.9.10/)
- [Django 3.2.16](https://docs.djangoproject.com/en/3.2/)
- [Django REST framework 3.12.4](https://github.com/ilyachch/django-rest-framework-rusdoc/tree/master)
- [DRF Simple JWT 4.7.2](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)

### Как запустить проект

Клонируйте репозитроий и перейдите в директорию `api_final_yatube`.

```bash
git clone git@github.com:Wiz410/api_final_yatube.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

- Для Windows `python`
- Для Linux macOS `python3`

```bash
python -m venv venv
```

- Для Windows

```bash
source venv/Scripts/activate
```

- Для Linux macOS

```bash
source venv/bin/activate
```

Установите зависимости из файла `requirements.txt`:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Перейдите в директорию `yatube_api`.

```bash
cd yatube_api
```

Выполните миграции и запустите проект.

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

### Примеры запросов

- Полная документация к запросам доступна по адресу `http://127.0.0.1:8000/redoc/`
- Количество запросов ограничено:
    - Для **авторизированных** пользователей **1000** в час.
    - Для **анонимных** **100** в час.

#### Создание нового поста
`POST` запрос на адрес: `http://127.0.0.1:8000/api/v1/posts/`
В поле `image` можно передать изображение в формате `Base64`
```json
{
    "text": "Тестовый пост"
}
```

```json
{
    "id": 1,
    "author": "TestUser",
    "text": "Тестовый пост",
    "pub_date": "2023-08-17T06:13:13.047944Z",
    "image": null,
    "group": null
}
```

#### Создание комментария к посту
`POST` запрос на адрес: `http://127.0.0.1:8000/api/v1/posts/id_поста/comments/`

```json
{
    "text": "Тестовый комментарий"
}
```

```json
{
    "id": 1,
    "author": "TestUser",
    "text": "Тестовый комментарий",
    "created": "2023-08-17T06:20:07.881765Z",
    "post": 1
}
```
#### Подписка на пользователя
`POST` запрос на адрес: `http://127.0.0.1:8000/api/v1/follow/`

```json
{
    "following": "Name"
}
```

```json
{
    "user": "TestUser",
    "following": "Name"
}
```

#### Авторы проекта

- [Yandex Practicum](https://github.com/yandex-praktikum)

- [Danila Polunin](https://github.com/Wiz410)