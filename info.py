import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#---------------------------------------------------------------
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '28631166'))
API_HASH = environ.get('API_HASH', 'dcf36e82600f9bc66857ae14607463c8')
BOT_TOKEN = environ.get('BOT_TOKEN', '7801211731:AAGlq0_iyCWNj4nV6s53QPtKSBUVK37_oyo')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7518064039').split()]
USERNAME = environ.get('USERNAME', "https://t.me/@Babita_jiii")  # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002559564172))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/movies_findr')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002545381881').split()]

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Raviii:Raviii@raviii.i9y7c.mongodb.net/?retryWrites=true&w=majority&appName=Raviii")
DATABASE_NAME = environ.get('DATABASE_NAME', "Ravi@12345")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', 0))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', 0))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS', 0))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', 0))
auth_channel = environ.get('AUTH_CHANNEL', '0')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', 0))
request_channel = environ.get('REQUEST_CHANNEL', '0')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/')  # Support group link (make sure bot is admin)

IS_VERIFY = is_enabled('IS_VERIFY', True)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9
