from src.Log import Log
from logging import WARN


class AnotherOneLog(Log):
    """Log Fluent Final Class

    Extends:
        src.Log.Log

    Returns:
        [AppLog] -- Log object
    """

    CONF = {
        'name': 'anotherone',
        'file': './logs/anotherone.log',
        'level': WARN,
        'format': "[%(asctime)s] %(message)s"
    }

    def __new__(cls):
        return super(AnotherOneLog, cls).__new__(cls, cls.CONF)

    def __init__(self):
        super(AnotherOneLog, self).__init__(name=self.CONF['name'])


    @classmethod
    def set_msg(cls, msg: str) -> Log:
        """
        Sets the log message

        :override
        :param msg: str
        :return Log: This class reference itself
        :rtype Logger
        """
        cls._instance._msg = f"'{str.lower(msg)}'"
        return cls