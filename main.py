import logging
from aiogram.utils.executor import start_webhook
from aiogram import executor

from bot.enums import StartType
from bot.loader import dp
from bot.config import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
from bot.utils import on_startup, on_shutdown


START_TYPE = StartType.webhook.value

logging.basicConfig(level=logging.DEBUG)

# TODO: Docs link:
# https://aiogram-birdi7.readthedocs.io/en/latest/examples/webhook_example_2.html


if __name__ == '__main__':
    if START_TYPE == StartType.polling.value:
        executor.start_polling(dp, on_startup=on_startup)

    if START_TYPE == StartType.webhook.value:
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )
