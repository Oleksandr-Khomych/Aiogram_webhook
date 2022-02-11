import logging

from aiohttp import web
from aiogram.dispatcher.webhook import get_new_configured_app
from bot.loader import dp
from bot.config import WEBAPP_PORT, WEBAPP_HOST, WEBHOOK_PATH
from bot.server_handlers import hello
from bot.utils import on_startup, on_shutdown


logging.basicConfig(level=logging.INFO)


# TODO: Docs link:
# https://aiogram-birdi7.readthedocs.io/en/latest/examples/webhook_example.html


if __name__ == '__main__':
    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_PATH)
    app.add_routes([web.get('/', hello)])

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
