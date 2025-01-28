from operator import add
import os
import logging
from os import environ

#import dotenv
#dotenv.load_dotenv()

from logging.handlers import RotatingFileHandler

# TRUE or FALSE
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "TRUE") == "TRUE" else False
U_S_E_P = True if (True if os.environ.get('U_S_E_P', "False") == "TRUE" else False) and USE_SHORTLINK else False
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "FALSE") == "TRUE" else False
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "TRUE") == "TRUE" else False
USE_PAYMENT = True if (True if os.environ.get("USE_PAYMENT", "TRUE") == "TRUE" else False) and USE_SHORTLINK else False
PINNED = True if os.environ.get("PINNED", "TRUE") == "TRUE" else False

PHOTO_URL = (environ.get('PHOTO_URL', '')).split()

# Force user to join your backup channel, leave 0 if you don't need.
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", ""))

# URLs are strings, so you may want to strip them in your main code
REQUEST1 = os.environ.get("REQUEST1", "")
REQUEST2 = os.environ.get("REQUEST2", "")

# Bot token, API ID, and hash
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "") 
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

# Other bot configurations
PORT = os.environ.get("PORT", "8000")
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "5"))
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link. 💾</b></blockquote>")
OWNER_TAG = os.environ.get("OWNER_TAG", "")
TIME = int(os.environ.get("TIME", "3600"))

    
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "86400"))
TUT_VID = os.environ.get("TUT_VID", "")

UPI_QR_CODE_URL = os.environ.get("UPI_QR_CODE_URL", "")


# Force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_MSG", "<blockquote><b>Hello {first}\n\nYou need to join in my Channel/Group to use me\n\nKindly Please join Channel</b></blockquote>🥺")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Admins
ADMINS = os.environ.get("ADMINS", "").split()
ADMINS.append(OWNER_ID)

# Logging configuration
LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
