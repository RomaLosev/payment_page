![example workflow](https://github.com/RomaLosev/payment_page/actions/workflows/main.yml/badge.svg)

# Описание проекта
Тестовое задание для ООО Ришат
Интеграция Django с сервисом приёма платежей stripe.com

# Установка проекта локально
Склонировать репозиторий и перейти в папку с проектом:
```sh
git clone git@github.com:RomaLosev/payment_page.git
cd payment_page
``` 
Cоздать и активировать виртуальное окружение:
```sh
python -m venv env
source env/bin/activate
```
Cоздайте файл .env в корневой директории с содержанием:
```sh
SECRET_KEY=секретный ключ django
DEBUG=False
STRIPE_PUBLIC_KEY='получить ключ в личном кабинете Stripe'
STRIPE_SECRET_KEY='получить ключ в личном кабинете Stripe'
```
Установить зависимости
```sh
pip install -r requirements.txt
```
Выполнить миграции:
```sh
python manage.py makemigrations
python manage.py migrate
```
Создать супервпользователя
```sh
python manage.py createsuperuser
```
Запустить сервер:
```sh
python manage.py runserver
```
Для отображения товаров нужно добавить их через админку django
```sh
http://127.0.0.1:8000/admin
```
Для работы оплаты необходимо добавить те же товары в личный кабинет stripe
```sh
https://dashboard.stripe.com/test/products
```
# Запуск проекта в Docker контейнере
Установить Docker с оф. сайта https://www.docker.com/
- Параметры запуска описаны в файлах docker-compose.yml и Dockerfile.


Запустить docker compose из корневой директории:
```sh
docker-compose up -d --build
```
Выполните миграции и создайте суперпользователя
```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuserdocker login -u billglasses
```

# Сайт
Готовый проект доступен по ссылке: http://51.250.16.28

# Автор
Лосев Р.Р. https://github.com/RomaLosev