# Онлайн магазин гаджетов на Django

Этот проект представляет собой онлайн-магазин гаджетов, разработанный с использованием фреймворка Django. Проект использует базу данных PostgreSQL и контейнеризацию с Docker для упрощения развертывания и настройки.

## Требования

Для запуска проекта необходимо:

1. Docker
2. Docker Compose
3. Python 3.12

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone <ссылка_на_репозиторий>
    cd <папка_с_проектом>
    ```

2. Создайте файл `.env` в корневой директории проекта. В этот файл необходимо добавить следующие переменные окружения:

    ```ini
    POSTGRES_DB=<название_базы_данных>
    POSTGRES_USER=<имя_пользователя_базы_данных>
    POSTGRES_PASSWORD=<пароль_к_базе_данных>
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432
    ```

    Замените значения на реальные данные для вашей базы данных PostgreSQL.

## Запуск проекта с использованием Docker

Проект использует Docker для контейнеризации. Для запуска проекта в Docker-контейнерах выполните следующие шаги:

1. Запустите контейнеры с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

    Эта команда создаст и запустит все необходимые контейнеры, включая Django приложение и PostgreSQL базу данных.

2. (Опционально) Создайте суперпользователя для админки Django:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

3. Откройте браузер и перейдите по адресу `http://localhost:8000/` для доступа к вашему онлайн-магазину.

    Для доступа к админке Django используйте `http://localhost:8000/admin/`.

## Завершение работы

Чтобы остановить и удалить контейнеры, выполните:

```bash
docker-compose down
