FROM python:3.10-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Создание директории приложения
WORKDIR /app

# Копирование requirements и установка зависимостей
COPY requirements.txt .

# Установка Python зависимостей
RUN pip install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Создание пользователя для безопасности
RUN useradd -m -u 1000 botuser && chown -R botuser:botuser /app
USER botuser

# Запуск бота
CMD ["python", "run_polling.py"]