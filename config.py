from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "25639252"))
API_HASH = getenv("API_HASH", "42db0fd56c51ff2b94cf064838eba7c1")

BOT_TOKEN = getenv("BOT_TOKEN", ")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://jembutan1:1234@cluster0.w186hoa.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 5061180769))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/stayheresay")
