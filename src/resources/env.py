from dotenv import dotenv_values

def read_values() -> dict:
    return dotenv_values("./.env")
    
IMAP_SERVER = read_values().get('IMAP_SERVER_HOST')
IMAP_PORT = read_values().get('IMAP_SERVER_PORT')

IMAP_USER = read_values().get('IMAP_SERVER_LOG')
IMAP_PWD = read_values().get('IMAP_SERVER_PWD')