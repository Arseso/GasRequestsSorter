from dataclasses import dataclass
from datetime import datetime

class LogGroup:
    """Groups for log strings"""
    IMAP = "IMAP"
    SMTP = "SMTP"
    NN = "NN"
    CORE = "CORE"
    
class LogType:
    ERROR = "ERROR"
    INFO = "INFO"

@dataclass
class LogMessage:
    type: str = LogType.INFO
    group: str = "NO GROUP"
    message: str = ""
    
    def build_string(self) -> str:
        return f"[{datetime.now()}][{self.group}][{self.type}] {self.message}"


    
# test = LogMessage()
# test.type = LogType.ERROR
# test.group = LogGroup.IMAP
# test.message = "Error"

# print(test.build_string())
