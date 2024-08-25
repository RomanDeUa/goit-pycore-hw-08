# Використовуйте офіційний образ Python як базовий
FROM python:3.12.1

# Встановіть робочу директорію всередині контейнера
WORKDIR /app

# Скопіюйте всі файли проекту до робочої директорії контейнера
COPY . /app

# Встановіть pipenv
RUN pip install pipenv

# Встановіть залежності проекту за допомогою pipenv
RUN pipenv install --deploy --ignore-pipfile

# Запустіть застосунок
CMD ["pipenv", "run", "python", "main.py"]

