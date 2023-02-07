# business-platform
Проект в разработке.

## Правила Git flow
- Ветка **master** тщательно оберегается от непроверенных изменений.
- Все свежие изменения вливаются в ветку **develop**. От неё ответвляем ветки для новых фичей.
- Ветки после слияния не удаляются.

## Установка и запуск приложения
- Скачать скрипт и распаковать архив
- Создать и активировать виртуальное окружение
- Установить зависимости: `pip install -r requirements.txt`

**Подробнее** (Видео): [смотреть >>>](https://t.me/andryplekhanov)

В репозитории уже находится тестовая база данных.
Можно сразу запускать: `python manage.py runserver`

И переходить по адресу: http://127.0.0.1:8000/

**Доступ в админку:** http://127.0.0.1:8000/admin/

Вход в админку с правами суперпользователя:
- **логин:** andryplekhanov
- **Пароль:** Aa25662566!
