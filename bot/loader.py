from aiohttp import web
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from bot.config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

app = web.Application()
