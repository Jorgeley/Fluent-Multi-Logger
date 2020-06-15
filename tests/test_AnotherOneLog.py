import pytest
import os
from datetime import datetime
from src.AnotherOneLog import AnotherOneLog
from src.Log import Log


def setup_function():
   pass


def teardown_function(cls):
    pass


def test_instance():
    assert isinstance(AnotherOneLog(), Log)


def test_msg():
    AnotherOneLog().set_msg('testing AnotherOneLog msg')
    assert AnotherOneLog()._msg == "'testing anotheronelog msg'"


def test_rotate():
    AnotherOneLog().rotate()
    size = os.path.getsize(AnotherOneLog()._config['file'])
    assert size == 0


def test_to_file():
    anotherOneLog = AnotherOneLog()
    anotherOneLog.rotate()
    '''
    this format should be created according to what specified in the AnotherOneLog.CONF atttribute,
    although not able to do it, needs more work around the logging.LogRecord class
    '''
    format = '[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + '] '
    anotherOneLog.set_msg('testing AnotherOneLog to file').to_file()
    config = anotherOneLog._config
    size = os.path.getsize(config['file'])
    assert size > 0
    log = open(config['file'], 'r')
    assert log.read() == format + anotherOneLog._msg + "\n"


def test_report():
    #I'm a lazy bastard
    pass


def test_send_log():
    # I'm a lazy bastard
    pass
