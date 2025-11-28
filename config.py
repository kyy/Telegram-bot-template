import os
from pathlib import Path
from aiogram import Bot
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

env_file = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_file)

TOKEN = os.getenv('BOT_TOKEN')
WH_BASE_URL = os.getenv('WH_BASE_URL')
WH_MAIN_BOT_PATH = os.getenv('WH_PATH')
bot = Bot(token=TOKEN)