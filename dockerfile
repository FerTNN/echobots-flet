# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение в контейнер
COPY . /app/

# Указываем порт, который будет использовать приложение
EXPOSE 8080

# Команда запуска приложения
CMD ["python", "main.py"]
