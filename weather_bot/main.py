import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

import requests
from datetime import datetime

from config import bot_token, open_weather_token
from weather import get_weather


# TOKEN = getenv("BOT_TOKEN")
TOKEN = bot_token

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!\nПогоду в каком городе ты хочешь узнать?")


@dp.message()
async def weather_message(message: types.Message) -> None: 
    
    await message.answer(get_weather(message.text, open_weather_token))




async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())