import asyncio
import logging
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.types import BotCommandScopeDefault
from config import bot
from commands import commands
from dp import dp_connector


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] [%(lineno)d] [%(name)s] [%(message)s]",
        # filename='polling.log',
        # filemode='a'
    )
    dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
    dp_connector(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")