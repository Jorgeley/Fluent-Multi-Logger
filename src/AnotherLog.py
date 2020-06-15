from src.Log import Log
from logging import INFO


class AnotherLog(Log):
    """Log Fluent Final Class

    Extends:
        src.Log.Log

    Returns:
        [AnotherLog] -- Log object
    """

    CONF = {
        'name': 'another',
        'file': './logs/another.log',
        'level': INFO,
        'format': "%(message)s"
    }

    def __new__(cls):
        return super(AnotherLog, cls).__new__(cls,  cls.CONF)

    def __init__(self):
        super(AnotherLog, self).__init__(name=self.CONF['name'])