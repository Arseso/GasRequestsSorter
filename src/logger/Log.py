import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s',
    level=logging.INFO
)

class Log:
    def __init__(self, name: str) -> None:
        self._logger = logging.getLogger(name=name)

    def info(self, string: str):
        self._logger.info(string)

    def error(self, string: str):
        self._logger.error(string)