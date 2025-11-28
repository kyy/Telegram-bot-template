import aiohttp
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command(commands=["weather"]))
async def cmd_weather(message: Message, state: FSMContext):
    await state.clear()  # Очищаем состояние

    try:
        # Получаем погоду для Минска
        weather_data = await get_weather("Minsk")

        if weather_data:
            response = (
                f"🌤 Погода в Минске:\n"
                f"📍 Температура: {weather_data['temperature']}°C\n"
                f"💧 Влажность: {weather_data['humidity']}%\n"
                f"🌬 Давление: {weather_data['pressure']} hPa\n"
                f"🌀 Ветер: {weather_data['wind_speed']} м/с\n"
                f"📝 Описание: {weather_data['description']}"
            )
        else:
            response = "❌ Не удалось получить данные о погоде"

    except Exception as e:
        response = f"⚠️ Произошла ошибка: {str(e)}"

    await message.answer(response)


async def get_weather(city: str) -> dict:
    url = f"https://wttr.in/{city}?format=j1"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                current = data['current_condition'][0]
                return {
                    'temperature': current['temp_C'],
                    'humidity': current['humidity'],
                    'pressure': current['pressure'],
                    'wind_speed': current['windspeedKmph'],
                    'description': current['weatherDesc'][0]['value']
                }
            return None