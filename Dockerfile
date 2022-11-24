FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml/ poetry.lock/ ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install
CMD ["gunicorn", "payment_page.wsgi:application", "--bind", "0:8000" ]