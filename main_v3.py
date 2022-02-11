# Use pyngrok
import logging

from aiohttp import web
from aiogram.dispatcher.webhook import get_new_configured_app
from pyngrok import ngrok

from bot.loader import dp
from bot.config import WEBAPP_PORT, WEBAPP_HOST, WEBHOOK_HOST, WEBHOOK_PATH, WEBHOOK_URL
from bot.server_handlers import hello
from bot.utils import on_shutdown, on_startup_ngrok


logging.basicConfig(level=logging.INFO)

USE_NGROK: bool = True


if __name__ == '__main__':
    if USE_NGROK:
        ngrok_conn = ngrok.connect(WEBAPP_PORT, bind_tls=True)
        https_url = ngrok_conn.public_url
        WEBHOOK_URL = WEBHOOK_URL.replace(WEBHOOK_HOST, https_url)

    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_PATH)
    app.add_routes([web.get('/', hello)])

    app.on_startup.append(on_startup_ngrok(WEBHOOK_URL))
    app.on_shutdown.append(on_shutdown)

    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
