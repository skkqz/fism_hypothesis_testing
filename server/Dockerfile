
#  Образ для python 3.12
FROM python:3.12-slim

# Устанавливаем зависимости для PostgreSQL и psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean

# Установка рабочей дериктории
WORKDIR /app

# Копирование файла с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Команда по умолчанию для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]