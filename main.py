from src.AppLog import AppLog
from src.AnotherLog import AnotherLog
from src.AnotherOneLog import AnotherOneLog

AppLog()\
    .set_msg('This is fluent multi logger project')\
    .to_screen()
AppLog()\
    .set_msg('this will be logged in a specific format and file according to what is defined in the AppLog class')\
    .to_screen()\
    .to_file()
AnotherLog()\
    .set_msg('this is a different log within different configuration')\
    .to_screen()\
    .to_file()
AnotherOneLog().set_msg('and this is another different log within different configurations')\
    .to_screen()\
    .to_file()
