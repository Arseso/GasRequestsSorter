from imap_tools import MailMessage
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
        
        for msg in self.client.fetch(mark_seen=False, bulk=10, limit=count, reverse=True):
            msgs.append(msg)
        
        logStringInfo.message = f"Recieved {len(msgs)} messages"
        printToLog(logStringInfo)
        return msgs
        
    def copy_msg(self, msg_uid: str, folder_destination: str) -> None:
        self.client.copy(uid_list=msg_uid, destination_folder= folder_destination)
        
        logStringInfo.message = f"Message uid {msg_uid} copied to folder [{folder_destination}]"
        printToLog(logStringInfo)
    
    def del_msg(self, msg_uid: str) -> None:
        self.client.delete(uid_list=msg_uid)
        logStringInfo.message = f"Message uid {msg_uid} deleted from folder [{self.get_current_folder()}]"
        printToLog(logStringInfo)

client = IMAPClientOperations()
client.set_folder('INBOX')
# client.set_folder('test3')

# client.copy_msg('3', 'test3')

msgs = client.get_folder_messages(count=1)
print(msgs[0].attachments)
print(msgs[0].flags)
print(msgs[0].headers)
print(msgs[0].reply_to)
# print("\n".join(str(msg.html) for msg in msgs))
# client.del_msg('5')

# print("\n".join(folder for folder in client.get_folders()))