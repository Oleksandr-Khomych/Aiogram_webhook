from aiogram import types
from aiogram.dispatcher.webhook import SendMessage

from bot.loader import dp   # , bot


@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)
    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)
