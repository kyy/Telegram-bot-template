from aiogram.dispatcher.dispatcher import Dispatcher
from middlewares import test_middlware
from handlers import (
    h_common,
    h_weather,
)


def dp_connector(dp: Dispatcher) -> Dispatcher:
    dp.update.middleware(test_middlware.TestMiddleware())
    dp.include_router(h_common.router)
    dp.include_router(h_weather.router)
    return dp