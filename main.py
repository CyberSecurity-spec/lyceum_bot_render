from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers

app = Client("lyceum_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
register_handlers(app)
print("🤖 Бот запущен!")
app.run()
