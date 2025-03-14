## Описание проекта
Веб-приложение генератор случайных чисел на FastAPI.

## Запуск
1. Соберите образ:
docker build -t fastapi-app .

2. Запустите контейнер:
docker run -p 8000:8000 fastapi-app

3. Откройте в браузере:
http://localhost:8000

## Запуск через Docker Compose (опционально)
docker-compose up --build

## Возможные ошибки
- **Address already in use** – убедитесь, что порт 8000 свободен.
- **ModuleNotFoundError** – убедитесь, что зависимости установлены.