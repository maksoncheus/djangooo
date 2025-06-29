# 1. Базовый образ
FROM python:3.11-slim

# 2. Устанавливаем переменные окружения, чтобы Python не буферизовал вывод
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Устанавливаем рабочую директорию
WORKDIR /app

# 4. Обновляем pip и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
