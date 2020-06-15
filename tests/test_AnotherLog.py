import pytest
import os
from src.AnotherLog import AnotherLog
from src.Log import Log


def setup_function():
   pass


def teardown_function(cls):
    pass


def test_instance():
    assert isinstance(AnotherLog(), Log)


def test_msg():
    AnotherLog().set_msg('testing AnotherLog msg')
    assert AnotherLog()._msg == 'testing AnotherLog msg'


def test_rotate():
    AnotherLog().rotate()
    size = os.path.getsize(AnotherLog()._config['file'])
    assert size == 0


def test_to_file():
    anotherLog = AnotherLog()
    anotherLog.rotate()
    anotherLog.set_msg('testing AnotherLog to file').to_file()
    config = anotherLog._config
    size = os.path.getsize(config['file'])
    assert size > 0
    log = open(config['file'], 'r')
    assert log.read() == anotherLog._msg + "\n"


def test_report():
    #I'm a lazy bastard
    pass


def test_send_log():
    # I'm a lazy bastard
    pass
