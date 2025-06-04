# Университет - система учёта успеваемости

## Функционал
- Управление студентами, предметами и оценками
- Просмотр средних баллов
- Отчёт об успеваемости (лучший/худший студент)
- Фильтрация и сортировка студентов

## Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать окружение: `source venv/bin/activate` (Linux/Mac) или `venv\Scripts\activate` (Windows)
4. Установить зависимости: `pip install -r requirements.txt`
5. Выполнить миграции: `python manage.py migrate`
6. Создать суперпользователя: `python manage.py createsuperuser`
7. Запустить сервер: `python manage.py runserver`

## Используемые технологии
- Python 3.10+
- Django 4.2
- Bootstrap 5