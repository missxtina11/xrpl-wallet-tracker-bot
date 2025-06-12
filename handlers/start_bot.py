import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command

load_dotenv()
BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("👋 Welcome to the Echo Protocol Wallet Tracker Bot!")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("📌 Commands: /balance, /tx, /created, /bubble, /ancestry, /liquidity, and more.")

async def run():
    await dp.start_polling(bot)
