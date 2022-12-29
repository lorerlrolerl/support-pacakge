"""
Author: Arash Yazdiha
The module defines a Logger class that can be used to customize the logging functionality
The formatting is defined here, but could also be set aside in a separate settings.
That can be done, but the formatting and colors are set according to preference.
To use this instantiate an object; Prior to that a root logger may be created
```
import logging
from support.logger import Logger

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
Logger()
```
"""
import logging
import logging.config
import os
import sys

import colorlog


class Logger:
    """Customizes the logging functionality based on a log config"""

    def __init__(self) -> None:
        self.logger = self._create_logger()
        self.folder = "logs"
        self.filename = self._get_filename()
        self.stream = "stderr"
        self.format = colorlog.ColoredFormatter(
            "%(log_color)-s%(asctime)-2s%(filename)-2s:%(lineno)d %(levelname)-5s%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,big_white",
            },
            secondary_log_colors={},
            style="%",
        )
        logging.captureWarnings(True)
        logging.config.dictConfig({"version": 1, "disable_existing_loggers": False})
        self.get_stream_handler()
        self.get_file_handler()

    @staticmethod
    def _create_logger() -> logging.Logger:
        logger = colorlog.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.handlers = []
        return logger

    @staticmethod
    def _get_filename() -> str:
        return os.path.basename(sys.argv[0])

    def get_stream_handler(self) -> None:
        """
        Adds a stream handler to the logger
        """
        stream_handler = colorlog.StreamHandler(getattr(sys, self.stream))
        stream_handler.setFormatter(self.format)
        self.logger.addHandler(stream_handler)

    def get_file_handler(self) -> None:
        """
        Adds a file handler to the logger
        """
        for level in ["WARNING", "ERROR", "CRITICAL"]:
            os.makedirs(self.folder, exist_ok=True)
            logfile_name = self.filename + "_" + level + ".log"
            file_handler = logging.FileHandler(
                os.path.join(self.folder, logfile_name), mode="w", delay=True
            )

            file_handler.setFormatter(self.format)
            file_handler.setLevel(getattr(logging, level))
            self.logger.addHandler(file_handler)
