from imap_tools import MailBox, AND
from src.resources import env

from src.logging.logging import printToLog
from src.models.logging.LogMessage import *

logStringInfo = LogMessage(group=LogGroup.IMAP, type=LogType.INFO)
logStringError = LogMessage(group=LogGroup.IMAP, type=LogType.ERROR)

class IMAPClientCore:
    
    client: MailBox
    
    def __init__(self):
        self._connect()
        self._login()
    
    def _connect(self):
        try:
            self.client = MailBox(host= env.IMAP_SERVER, port=env.IMAP_PORT)
            logStringInfo.message = f"Connected to {env.IMAP_SERVER}:{env.IMAP_PORT}"
            printToLog(logStringInfo)
        except:
            logStringInfo.message = f"Error while connecting to server"
            printToLog(logStringError)
            
    def _login(self):
        try:
            self.client.login(env.IMAP_USER, env.IMAP_PWD)
            logStringInfo.message = f"Login successfully"
            printToLog(logStringInfo)
        except:
            logStringInfo.message = f"Error while login"
            printToLog(logStringError)
            

# client = IMAPClientCore()
# print("\n".join(f"{folder.name}" for folder in client.client.folder.list()))
# print(",".join(msg.flags for msg in client.client.fetch()))