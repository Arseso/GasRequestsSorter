from imap_tools import AND, MailMessage

from src.imap.IMAPClientCore import IMAPClientCore



class IMAPClientOperations(IMAPClientCore):
    def __init__(self):
        super().__init__()
    
    def get_by_uid(self, uid: str) -> MailMessage:
        for msg in self.client.fetch(AND(uid=uid)):
            return msg
        
    def get_folder(self, folder_name: str, count: int = -1) -> list[MailMessage]:
        msgs = []
        cur_folder = self.client.folder.get()
        
        self.client.folder.set(folder= folder_name)
        
        for msg in self.client.fetch():
            msgs.append(msg)
        
        