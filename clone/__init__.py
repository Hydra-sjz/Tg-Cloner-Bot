
import logging
from os import environ, mkdir, path, sys

from dotenv import load_dotenv
from pyrogram import Client


# Log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)



API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
BOT_TOKEN = environ["BOT_TOKEN"]


#os.system("apt install git curl python3-pip ffmpeg -y")

class Mbot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir="./cache/",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            sleep_threshold=30,
        )

    async def start(self):
        global BOT_INFO
        await super().start()
        BOT_INFO = await self.get_me()
        if not path.exists("/tmp/thumbnails/"):
            mkdir("/tmp/thumbnails/")
        for chat in AUTH_CHATS:
            await self.send_photo(
                chat,
                "https://telegra.ph/file/2b49eab80cc0efddf5515.jpg",
                "Bot Started.",
            )
        LOGGER.info(f"Music X dlBot Started As {BOT_INFO.username}\n")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("Bot Stopped, Bye.")
