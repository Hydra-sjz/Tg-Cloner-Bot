import os
from os import getenv
from dotenv import load_dotenv
from os import environ

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
AUTH_CHATS = environ.get("AUTH_CHATS", "").split()
AUTH_CHATS = [int(_x) for _x in AUTH_CHATS]
