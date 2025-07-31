from src.models.logging.LogMessage import *
import sys

def _init_log_file():
    pass

def _print_to_file(msg: LogMessage):
    pass

def _print_to_console(msg: LogMessage):
    if msg.type == LogType.ERROR:
        print(msg.build_string(), file=sys.stderr)
        return
    print(msg.build_string(), file=sys.stdout)
    
def printToLog(msg: LogMessage):
    _print_to_console(msg)
    _print_to_file(msg)