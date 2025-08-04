from dataclasses import dataclass

@dataclass
class Message:
    uid: str
    subject: str = ""
    body: str = ""
    tags: list[str] = None
    
    def as_plain(self) -> str:
        return f"""[S]{self.subject}[EOS]\
[B]{self.body}[EOB]\
[T]{"".join(f"{{{tag}}}" for tag in self.tags)}[EOT]"""
        
# m = Message()
# m.subject = "S"
# m.body = "B"
# m.tags = ["T1", "T2", "T3"]

# print(m.as_plain())