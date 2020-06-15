import pytest
import os
from datetime import datetime
from src.AppLog import AppLog
from src.Log import Log


def setup_function():
   pass


def teardown_function(cls):
    pass


def test_instance():
    assert isinstance(AppLog(), Log)


def test_msg():
    AppLog().set_msg('testing AppLog msg')
    assert AppLog()._msg == 'testing AppLog msg'


def test_rotate():
    AppLog().rotate()
    size = os.path.getsize(AppLog()._config['file'])
    assert size == 0


def test_to_file():
    appLog = AppLog()
    appLog.rotate()
    '''
    this format should be created according to what specified in the AppLog.CONF atttribute,
    although not able to do it, needs more work around the logging.LogRecord class
    '''
    format = '[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + '] DEBUG - ' + os.path.abspath('src/Log.py') + ':to_file() -> '
    appLog.set_msg('testing AppLog to file').to_file()
    config = appLog._config
    size = os.path.getsize(config['file'])
    assert size > 0
    log = open(config['file'], 'r')
    assert log.read() == format + appLog._msg + "\n"


def test_report():
    #I'm a lazy bastard
    pass


def test_send_log():
    # I'm a lazy bastard
    pass
