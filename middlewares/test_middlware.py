from aiogram import BaseMiddleware

class TestMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        data['test'] = 'test'
        return await handler(event, data)