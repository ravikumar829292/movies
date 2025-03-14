import re
from os import environ

# Regex pattern to match IDs
id_pattern = re.compile(r'^.\d+$')

# Function to check if a value is enabled
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#---------------------------------------------------------------
# Bot configuration
SESSION = environ.get('SESSION', 'Media_search')  # Session name
API_ID = int(environ.get('API_ID', '28631166'))  # Telegram API ID
API_HASH = environ.get('API_HASH', 'dcf36e82600f9bc66857ae14607463c8')  # Telegram API Hash
BOT_TOKEN = environ.get('BOT_TOKEN', '7801211731:AAGlq0_iyCWNj4nV6s53QPtKSBUVK37_oyo')  # Bot token

# Admins and channels
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7518064039').split()]
USERNAME = environ.get('USERNAME', "https://t.me/@Babita_jiii")  # Admin username
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002559564172'))  # Log channel ID
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/movies_findr')  # Movie group link
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002545381881').split()]

# Database configuration
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Raviii:Raviii@raviii.i9y7c.mongodb.net/?retryWrites=true&w=majority&appName=Raviii")
DATABASE_NAME = environ.get('DATABASE_NAME', "Ravi@12345")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Additional channels
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '0'))  # API log channel
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '0'))  # Bin channel
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS', '0'))  # Delete channels
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))  # VR log channel
auth_channel = environ.get('AUTH_CHANNEL', '0')  # Auth channel
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None  # Convert to int if valid
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))  # Support group ID
request_channel = environ.get('REQUEST_CHANNEL', '0')  # Request channel
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None  # Convert to int if valid
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '0'))  # Movie update channel
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/')  # Support chat link

# Verification and shortener configuration
IS_VERIFY = is_enabled('IS_VERIFY', True)  # Enable verification
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")  # Tutorial link
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")  # Verification image
SHORTENER_API = environ.get("SHORTENER_API", "3097623f852197a9ce40d1212aaa8bbf2803e799")  # Shortener API
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'omegalinks.in')  # Shortener website
SHORTENER_API2 = environ.get("SHORTENER_API2", "3097623f852197a9ce40d1212aaa8bbf2803e799")  # Second shortener API
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'omegalinks.in')  # Second shortener website
SHORTENER_API3 = environ.get("SHORTENER_API3", "3097623f852197a9ce40d1212aaa8bbf2803e799")  # Third shortener API
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'omegalinks.in')  # Third shortener website
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))  # Two-step verification gap
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))  # Three-step verification gap

# Media and quality settings
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip", "web-dl", "bluray", "hdr", "fhd", "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024, 2002, -1)]
SEASONS = [f'season {i}' for i in range(1, 23)]
REF_PREMIUM = 30  # Referral premium
PREMIUM_POINT = 1500  # Premium points

# Images and media
START_IMG = environ.get('START_IMG', 'https://i.ibb.co/qpxpGmC/image.jpg https://i.ibb.co/DQ35zLZ/image.jpg').split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = environ.get("REFER_PICS", "https://envs.sh/PSI.jpg").split()
PAYPICS = environ.get('PAYPICS', 'https://envs.sh/_kA.jpg').split()
SUBSCRIPTION = environ.get('SUBSCRIPTION', 'https://graph.org/file/9f3f47c690bbcc67633c2.jpg')
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]

# Bot behavior settings
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))  # Auto-delete timer
AUTO_FILTER = is_enabled('AUTO_FILTER', True)  # Enable auto-filter
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)  # Enable PM search
PORT = environ.get('PORT', '5000')  # Port for the bot
MAX_BTN = int(environ.get('MAX_BTN', '8'))  # Maximum buttons
AUTO_DELETE = is_enabled('AUTO_DELETE', True)  # Enable auto-delete
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))  # Delete time
IMDB = is_enabled('IMDB', False)  # Enable IMDB
FILE_CAPTION = environ.get('FILE_CAPTION', '')  # File caption
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', '')  # IMDB template
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)  # Long IMDB description
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)  # Protect content
SPELL_CHECK = is_enabled('SPELL_CHECK', True)  # Enable spell check
LINK_MODE = is_enabled('LINK_MODE', True)  # Enable link mode

# Stream mode
STREAM_MODE = bool(environ.get('STREAM_MODE', True))  # Enable stream mode
MULTI_CLIENT = False  # Multi-client mode
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))  # Sleep threshold
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # Ping interval (20 minutes)

# Heroku deployment
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")  # Fully Qualified Domain Name

# Settings dictionary
SETTINGS = {
    'spell_check': SPELL_CHECK,
    'auto_filter': AUTO_FILTER,
    'file_secure': PROTECT_CONTENT,
    'auto_delete': AUTO_DELETE,
    'template': IMDB_TEMPLATE,
    'caption': FILE_CAPTION,
    'tutorial': TUTORIAL,
    'shortner': SHORTENER_WEBSITE,
    'api': SHORTENER_API,
    'shortner_two': SHORTENER_WEBSITE2,
    'api_two': SHORTENER_API2,
    'log': LOG_VR_CHANNEL,
    'imdb': IMDB,
    'link': LINK_MODE,
    'is_verify': IS_VERIFY,
    'verify_time': TWO_VERIFY_GAP,
    'shortner_three': SHORTENER_WEBSITE3,
    'api_three': SHORTENER_API3,
    'third_verify_time': THREE_VERIFY_GAP
}
