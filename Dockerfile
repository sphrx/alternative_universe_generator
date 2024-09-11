# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock* ./

# Устанавливаем poetry и зависимости
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Копируем остальные файлы проекта
COPY . .

# Создаем директории для входных и выходных файлов
RUN mkdir -p /app/files_input /app/files_output

# Запускаем приложение
CMD ["python", "main.py"]