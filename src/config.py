import os
from pathlib import Path
from dotenv import load_dotenv
from .logger import Log

_log = Log("Config")

if load_dotenv(Path(__file__).parent / ".env"): 
    _log.info(".env loaded")
else:
    _log.error(".env file not found")


class ENV:
    class SERVER:
        HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
        PORT: int = int(os.getenv("SERVER_PORT", "8000"))

    class TASKMNGR:
        HOST: str = os.getenv("TASKMNGR_HOST", "taskmngr")
        PORT: int = int(os.getenv("TASKMNGR_PORT", "6379"))
        USER: str = os.getenv("TASKMNGR_USR", "taskmngr")
        PASSWORD: str = os.getenv("TASKMNGR_PWD", "taskmngr")



