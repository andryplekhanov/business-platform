## Установка и запуск приложения
- Скачать скрипт и распаковать архив
- Создать и активировать виртуальное окружение
- Установить зависимости: `pip install -r requirements.txt`
- Установить фикстуры (там важные для работы приложения данные): `python manage.py loaddata fixtures/db.json`


Вход в админку с правами суперпользователя:
- **логин:** andryplekhanov@rambler.ru
- **Пароль:** Aa25662566!

## Деплойт
При деплойте вы столкнётесь с парой ошибок связанных с работой ‘django.contrib.sites'.
Вы должны войти в шелл (python manage.py shell) и написать следующие команды:
- `from django.contrib.sites.models import Site`
- `site = Site.objects.create(domain='http://ваш_домен.ru/', name=''http://ваш_домен.ru/)`
- `site.save()`
