#(©)CodeXBotz
#By @Codeflix_Bots



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21366247"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1d6666d32848a6878c191167a491205d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002204674963"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://indumati:indumati@cluster0.o3zeumz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002246485177"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002096532789"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002172897126"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n ɪ ᴀᴍ ᴍᴜʟᴛɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ » @team_netflix</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5239113414 7323409831").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝙎𝙪𝙣𝙣𝙖 {first} 𝙔𝙚 3 𝘾𝙝𝙖𝙣𝙣𝙚𝙡𝙨 𝙟𝙤𝙞𝙣 𝙠𝙖𝙧𝙡𝙚 𝙛𝙞𝙧 𝙝𝙚 𝙩𝙪𝙟𝙞 𝙢𝙖𝙖𝙡 𝙢𝙞𝙡𝙚𝙜𝙖..\n\n𝘼𝙪𝙧 𝙅𝙤𝙞𝙣 𝙠𝙖𝙧 𝙣𝙚 𝙗𝙖𝙙𝙖𝙢𝙚 𝙞𝙨𝙥𝙚 𝘾𝙡𝙞𝙘𝙠 𝙠𝙖𝙧 “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝘽𝙪𝙩𝙩𝙤𝙣....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» BY @dholakpur_admin</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝙆𝙮𝙪𝙪 𝘽𝙤𝙩 𝙠𝙚 𝙜𝙖𝙣𝙙 𝙢𝙖𝙧 𝙧𝙖𝙝 𝙝𝙪 𝙗𝙝𝙖𝙞..\n\n𝙢𝙖𝙩 𝙠𝙖𝙧𝙤 𝙢𝙨𝙜 𝙮𝙚 𝙥𝙚 𝙢𝙖𝙖𝙡 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙥𝙚 𝙝𝙖𝙞"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "codeflixbots.txt"

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
