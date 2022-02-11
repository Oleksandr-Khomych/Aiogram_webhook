import logging
from typing import Optional, Callable
import functools
from aiogram.dispatcher.dispatcher import Dispatcher

from bot.loader import bot
from bot.config import WEBHOOK_URL, admin_id


async def on_startup(dp: Dispatcher):
    # Connect message handlers
    from bot import handlers

    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start
    me = await bot.me
    await bot.send_message(admin_id, f'✅ <b>{me.first_name} ({me.username})</b> start!', parse_mode='HTML')


async def on_shutdown(dp: Dispatcher):
    logging.warning('Shutting down..')
    # insert code here to run it before shutdown
    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()
    logging.warning('Bye!')


def on_startup_ngrok(new_url: Optional[str] = None):
    if new_url:
        WEBHOOK_URL = new_url

    async def wrapper(*args, **kwargs):
        # Connect message handlers
        from bot import handlers
        logging.info(f'{WEBHOOK_URL=}')
        await bot.set_webhook(WEBHOOK_URL)
        # insert code here to run it after start
        me = await bot.me
        await bot.send_message(admin_id, f'✅ <b>{me.first_name} ({me.username})</b> start!', parse_mode='HTML')

    return wrapper
