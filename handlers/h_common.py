from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(f"Привет")


