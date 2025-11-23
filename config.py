import os

class Config(object):
    BOT_TOKEN = os.environ.get("")
    API_ID = int(os.environ.get("27765349"))
    API_HASH = os.environ.get("9df1f705c8047ac0d723b29069a1332b")
    AUTH_USER = os.environ.get('1116405290').split(',')
    AUTH_USERS = [1116405290]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[AJ]"

