from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("TOKEN")

# webhook settings
WEBHOOK_HOST = "https://your.domain"
WEBHOOK_PATH = f"/path/to/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = 3001

admin_id = env.str("admin_id")
