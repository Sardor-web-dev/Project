import logging
import sys

def setup_logger() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        stream=sys.stdout,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%M-%D %H:%M:%S"
    )