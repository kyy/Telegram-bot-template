import logging
from typing import Any, Dict, Union

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.utils.token import TokenValidationError, validate_token
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp import web
from config import TOKEN, WH_BASE_URL, WH_MAIN_BOT_PATH
from commands import commands
from dp import dp_connector


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(lineno)d] [%(name)s] [%(message)s]",
    # filename='webhook.log',
    # filemode='a'
)

"""
Быстрая проверка вебхука через локальное туннелирование
npm install -g localtunnel
lt --port 8888
копируем полученный домен в .env WH_BASE_URL
WH_PATH= оставляем пустым
запускаем python run_webhook.py
"""
PORT=8888
BASE_URL: str = WH_BASE_URL
MAIN_BOT_PATH: str = WH_MAIN_BOT_PATH


def is_bot_token(value: str) -> Union[bool, Dict[str, Any]]:
    try:
        validate_token(value)
    except TokenValidationError:
        return False
    return True


async def on_startup(bot: Bot):
    await bot.set_webhook(f"{BASE_URL}{MAIN_BOT_PATH}")
    await bot.set_my_commands(commands=commands)


def webhook():
    app = web.Application()
    session = AiohttpSession()
    bot_settings = {
        "token": TOKEN, "session": session,
        "default": DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        )
    }
    bot = Bot(**bot_settings)
    dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)  # FSM !
    dp.startup.register(on_startup)
    dp_connector(dp)
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=MAIN_BOT_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host='0.0.0.0', port=PORT)


if __name__ == "__main__":
    webhook()