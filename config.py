from secrets import UserConfig
import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or UserConfig.SECRET_KEY
