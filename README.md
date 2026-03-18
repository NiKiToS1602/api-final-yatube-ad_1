# Yatube API (final)

REST API для учебного проекта **Yatube**: посты, группы, комментарии и подписки.
Аутентификация реализована через **JWT-токены**.

## Возможности

- **Посты**: просмотр, создание, редактирование и удаление.
- **Комментарии**: вложенные в посты (`/posts/{post_id}/comments/`).
- **Группы**: только чтение (создаются через админку).
- **Подписки**: `/follow/` — доступен **только авторизованным**; есть поиск `?search=`.

## Права доступа

- **Анонимные пользователи**: доступ только на чтение.
- **Авторизованные пользователи**: могут создавать контент и изменять/удалять **только свой**.
- **Исключение**: эндпоинт **`/follow/`** доступен только авторизованным (и на чтение, и на запись).

## Установка и запуск (локально)

```bash
python -m venv venv
```

Windows:

```bash
venv\\Scripts\\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Миграции:

```bash
python yatube_api/manage.py migrate
```

Запуск сервера разработки:

```bash
python yatube_api/manage.py runserver
```

Документация (ReDoc): `http://127.0.0.1:8000/redoc/`

## Примеры запросов к API

Базовый префикс: `/api/v1/`

### Получить JWT-токен

`POST /api/v1/jwt/create/`

```json
{
  "username": "TestUser",
  "password": "1234567"
}
```

Ответ:

```json
{
  "refresh": "…",
  "access": "…"
}
```

Дальше передавайте токен:

`Authorization: Bearer <access>`

### Посты

- `GET /api/v1/posts/` — список постов
- `POST /api/v1/posts/` — создать пост (только auth)

Пример тела для создания:

```json
{
  "text": "Мой пост",
  "group": 1
}
```

### Комментарии к посту

- `GET /api/v1/posts/1/comments/`
- `POST /api/v1/posts/1/comments/` (только auth)

```json
{
  "text": "Комментарий"
}
```

### Группы

- `GET /api/v1/groups/`
- `GET /api/v1/groups/1/`

### Подписки

- `GET /api/v1/follow/` — мои подписки (только auth)
- `GET /api/v1/follow/?search=TestUser2` — поиск по `following`
- `POST /api/v1/follow/` — подписаться (только auth)

```json
{
  "following": "TestUser2"
}
```

