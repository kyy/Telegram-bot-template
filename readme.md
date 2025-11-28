## Установка и настройка

### Создайте файл .env в корне проекта
BOT_TOKEN=токен бота

#### Переменные необходимые для вебхука:

WH_BASE_URL=https://mydomen.by
WH_PATH=адрес вебхука (пример: /secret-webhook-of-my-telegram-bot)

### Создайте и активируйте виртуальное окружение
`python -m venv venv`

Для Windows:
`venv\Scripts\activate`

Для Linux/MacOS:
`source venv/bin/activate`

### Обновите pip и установите зависимости
`python -m pip install --upgrade pip`

`pip install --upgrade wheel`

`pip install -r requirements.txt`