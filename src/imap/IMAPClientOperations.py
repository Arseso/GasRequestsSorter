from imap_tools import AND, MailMessage
from tqdm import tqdm
from src.imap.IMAPClientCore import IMAPClientCore

from src.logging.logging import printToLog
from src.models.logging.LogMessage import *

logStringInfo = LogMessage(group=LogGroup.IMAP, type=LogType.INFO)
logStringError = LogMessage(group=LogGroup.IMAP, type=LogType.ERROR)


class IMAPClientOperations(IMAPClientCore):
    def __init__(self):
        super().__init__()
    
    def set_folder(self, folder_name: str) -> None:
        self.client.folder.set(folder_name)
        logStringInfo.message = f"Changed folder to [{folder_name}]"
        printToLog(logStringInfo)
        
    def get_folder_messages(self, count: int | None = None) -> list[MailMessage]:
        msgs = []
        
        for msg in self.client.fetch(mark_seen=False, bulk=10):
            msgs.append(msg)
        
        logStringInfo.message = f"Recieved {len(msgs)} messages"
        printToLog(logStringInfo)
        return msgs
        
    def copy_msg(self, msg_uid: str, folder_destination: str):
        self.client.copy(uid_list=msg_uid, destination_folder= folder_destination)
        
        logStringInfo.message = f"Message uid {msg_uid} copied to folder [{folder_destination}]"
        printToLog(logStringInfo)

# client = IMAPClientOperations()
# client.set_folder('тест')
# # msgs = client.get_folder_messages()
# # print(client.get_current_folder())
# # print(" ".join(msg.uid for msg in msgs))

# client.copy_msg('1', 'test3')