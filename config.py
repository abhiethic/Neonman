#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", 17107151))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e8ef290caf40133405160fdc0fabcbee")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ))

#Port
PORT = os.environ.get("PORT", 8080)

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "SUPERHERE-DB")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # token expiration time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/The_How_To_Open/13")
# warning !! not for kidz
TIME_TO_DEL = int(os.environ.get("TIME_TO_DEL", 3600))

#force sub channel id, if you want to enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", 0))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋 Hello... {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It Through A Special Link. 🔗")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7981975454 7554815378").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins List Doesn't Contain Valid Integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello... {mention}\n\n<b>You Must Join My Channel/Group To Use Me ⚡</b>")

#set your Custom Caption here, Keep None to Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>😴 Haven't Slept Since : </b>{uptime}"
try:
    USER_REPLY_TEXT = []
    for uwu in (os.environ.get("USER_REPLY_TEXT", "❌ Don't Send Me Messages Directly, I'm Only File Share Bot !!|Are You Komedi Me? 😂|Really Nigga? 🗿| Don't Try This Kid!|Go and Enjoy Your Video 😒|HaHa You Noob😂").split("|")):
        USER_REPLY_TEXT.append(str(uwu))
except Exception as uff:
        raise Exception("Error: " + str(uff))

ADMINS.append(OWNER_ID)
ADMINS.append(7554815378)

LOG_FILE_NAME = "filesharingbot.txt"

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
