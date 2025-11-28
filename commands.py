from aiogram.types import BotCommand

commands = [
    BotCommand(
        command="/start",
        description="📋  Привет",
        full_description=" Привет"
    ),
    BotCommand(
        command="/weather",
        description="📋  Погода",
        full_description=" Показать погоду в Минске"
    ),
]