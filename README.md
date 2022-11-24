![example workflow](https://github.com/RomaLosev/payment_page/actions/workflows/main.yml/badge.svg)

# Описание проекта
Тестовое задание
-
Интеграция Django с сервисом приёма платежей stripe.com
- Сделаны все доп. задания, кроме payment-intent
- Есть три простеньких html странички для оплаты одного товара.
- Сформировать заказ можно только через админку
- Прикрутить к заказу скидку и налог тоже только через админку

# Сайт
Готовый проект доступен по адресам:
- http://84.201.165.109 Главная страница со всеми товарами
- GET http://84.201.165.109/buy/{id}  - Возвращает session.id для оплаты одного товара
- GET http://84.201.165.109/item/{id} - Html страница с выбранным товаром
(при нажатии на кнопку происходит редирект на форму оплаты stripe)
- GET http://84.201.165.109/order/{id} - Аналогично предыдущей, но с оплатой заказа
(При нажатии на кнопку происходит редирект на форму оплаты stripe)
- GET http://84.201.165.109/pay_for_order/{id} - Возвращает session.id для оплаты заказа
(Если к заказу прикреплены Скидка или Налог, они добавляются автоматически)

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
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST='127.0.0.1'
DB_PORT=5432
```
Для работы базы данных запустить её в Docker
```sh
docker run \
  --rm   \
  --name postgres \
  -p 5432:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=collection \
  -d postgres:14.5
```

Установить poetry
```sh
pip install poetry
```
Установить зависимости
```sh
poetry install
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
- Параметры запуска описаны в файлах docker-compose.yaml и Dockerfile.

Запустить docker compose из корневой директории:
```sh
docker-compose up -d --build
```
Выполните миграции и создайте суперпользователя
```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

# Автор
Лосев Р.Р. https://github.com/RomaLosev