from __future__ import annotations
from abc import ABC
from logging import Logger, StreamHandler, getLogger, Formatter
from logging.handlers import RotatingFileHandler
from smtplib import SMTP, SMTPConnectError, SMTPNotSupportedError
import os
from builtins import ConnectionRefusedError


class Log(ABC, Logger):
    """Log Fluent Final Class

    Extends:
        logging.Logger

    Returns:
        [Log] -- Log object
    """

    _instance = None

    _logger = None

    _config = None

    _msg = ''

    def __new__(self, config):
        """Singleton
        """
        if not self._instance:
            self._instance = super(Log, self).__new__(self)
            self._instance._config = config
            self._instance._logger = getLogger(self._instance._config['name'])
            self._instance._logger.setLevel(self._instance._config['level'])
            handler = RotatingFileHandler(filename=self._instance._config['file'], maxBytes=100000000, backupCount=1)
            formatter = Formatter(self._instance._config['format'])
            handler.setFormatter(formatter)
            self._instance._logger.addHandler(handler)
        return self._instance

    @classmethod
    def set_msg(cls, msg: str) -> Log:
        """
        Sets the log message

        :param msg: str
        :return Log: This class reference itself
        :rtype Logger
        """
        cls._instance._msg = msg
        return cls

    @classmethod
    def to_file(cls) -> Log:
        """
        Output the log message to file

        :return Log: This class reference itself
        :rtype Logger
        """
        cls._instance._logger.log(cls._instance._logger.level, cls._instance._msg)
        return cls

    @classmethod
    def to_screen(cls) -> Log:
        """
        Output the log message to screen

        :return Log: This class reference itself
        :rtype Logger
        """
        for hdlr in cls._instance._logger.handlers:
            if type(hdlr) == StreamHandler:
                return cls
        ch = StreamHandler()
        cls._instance._logger.addHandler(ch)
        return cls

    @classmethod
    def rotate(cls) -> Log:
        """
        force rotation of the log

        :return: Log: this class reference itself
        :rtype Logger
        """
        cls._instance._logger.handlers[0].doRollover()
        return cls

    @classmethod
    def log_exception(cls, msg_) -> Log:
        """
        Log an exception

        :param msg_: The string message to be logge
        :return: Log: this class reference itself
        """
        cls._instance._msg = str(msg_)
        cls._instance._logger.exception(msg=msg_, exc_info=True)
        return cls

    @classmethod
    def get_log_path(cls) -> str:
        """
        Gets the log path

        :return cls._config['file']: The directory path
        :rtype str
        """
        return cls._config['file']

    @classmethod
    def __check_log_dir(cls) -> None:
        """
        Check if the log dir exists, if not, try to create it

        :rtype None
        """
        try:
            if not os.path.exists(os.environ['LOG_DIR']):
                os.makedirs(os.environ['LOG_DIR'])
        except PermissionError:
            print("Unable to create log dirs due to permission issues, you'll have to create them manually, see .env")

    @classmethod
    def send_log(cls, subject: str, body: str) -> None:
        """
        Sends a log via email

        :param subject: The subject of the email
        :param body: The body of the email
        :return:
        """
        if os.path.getsize(cls._instance._config['file']) > 0:
            from email.message import EmailMessage
            msg = EmailMessage()
            #you have to define this environment variable yourself!
            msg['From'] = os.environ['ALERTS_EMAIL']
            msg['To'] = os.environ['ALERTS_EMAIL']
            msg['Subject'] = subject
            msg.set_content(body)
            with open(cls._instance._config['file'], 'rb') as fp:
                data = fp.read()
            msg.add_attachment(data, maintype='text', subtype='plain')
            try:
                with SMTP(os.environ['SMTP_SERVER']) as s:
                    s.send_message(msg)
            except SMTPConnectError:
                cls.log_exception('Issue with SMTP server').to_screen()
            except ConnectionRefusedError:
                cls.log_exception('Connection refused').to_screen()
            except ValueError:
                cls.log_exception('Something wrong with message composition').to_screen()
            except SMTPNotSupportedError:
                cls.log_exception('Issue with servers communication').to_screen()