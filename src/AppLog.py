from src.Log import Log
from logging import DEBUG


class AppLog(Log):
    """Log Fluent Final Class

    Extends:
        src.Log.Log

    Returns:
        [AppLog] -- Log object
    """

    CONF = {
        'name': 'app',
        'file': './logs/app.log',
        'level': DEBUG,
        'format': "[%(asctime)s] %(levelname)s - %(pathname)s:%(funcName)s() -> %(message)s",
    }

    def __new__(cls):
        return super(AppLog, cls).__new__(cls,  cls.CONF)

    def __init__(self):
        super(AppLog, self).__init__(name=self.CONF['name'])