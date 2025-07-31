from dotenv import dotenv_values

def _read_values() -> dict:
    return dotenv_values("./.env")
    
IMAP_SERVER = _read_values().get('IMAP_SERVER_HOST')
IMAP_PORT = _read_values().get('IMAP_SERVER_PORT')

IMAP_USER = _read_values().get('IMAP_SERVER_LOG')
IMAP_PWD = _read_values().get('IMAP_SERVER_PWD')