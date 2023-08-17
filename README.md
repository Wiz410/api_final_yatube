# api_final
**Api final** учебный проект 11 спринта в **yandex practicum**.

### Требование

- Python 3.9.10


### Как запустить проект

- [Для Windows](guide/win.md)

- [Для Linux/macOS](guide/linux_macos.md)

### Примеры запросов

- [Большинство запросов доступны только с jwt токеном.](guide/token.md)
- Полная документация к запросам доступна по адресу `http://127.0.0.1:8000/redoc/`

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