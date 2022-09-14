FROM python:3.10.6-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "payment_page.wsgi:application", "--bind", "0:8000" ]