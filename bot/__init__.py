import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "36072133"))
    API_HASH = os.environ.get("API_HASH", "17fde35cd8b2d88fa1ee0c9984bc49bf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8612783599:AAEwjcmQqqtcGNq2PadkV9hNbpb2A9mP-5Q")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "manishsharmabot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
