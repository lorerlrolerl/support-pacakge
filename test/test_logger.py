"""
To Test logger functionality
"""
import logging

import support

# import pytest


def main() -> None:
    """
    test logger
    """
    support.Logger()
    logging.info("Info")
    logging.debug("Debug")
    logging.error("Error")
    logging.critical("Critical")
    logging.warning("Warning")


if __name__ == "__main__":
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    main()
