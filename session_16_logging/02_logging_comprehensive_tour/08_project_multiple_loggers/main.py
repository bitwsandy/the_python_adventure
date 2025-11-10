# main.py
import logging
from logging import StreamHandler, FileHandler, Formatter
import sys
import utils

"""
Root-logger configuration (one place only).
All module loggers (created via getLogger(__name__)) will inherit this.
We attach TWO handlers to the *root* logger:
  - Console (StreamHandler)
  - File (FileHandler -> logs/app.log)
"""

def setup_logging():
    # 1) Get the ROOT logger
    root = logging.getLogger()          # root logger has empty name ""
    root.setLevel(logging.DEBUG)        # Let root accept everything; handlers will filter

    # 2) Avoid duplicate handlers if this runs multiple times (e.g., notebooks)
    if root.handlers:
        root.handlers.clear()

    # 3) Create handlers
    console = StreamHandler(stream=sys.stdout)
    console.setLevel(logging.INFO)      # Show INFO+ on console

    file = FileHandler("app.log", encoding="utf-8")
    file.setLevel(logging.DEBUG)        # Capture DEBUG+ in file

    # 4) Common formatter
    fmt = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    console.setFormatter(fmt)
    file.setFormatter(fmt)

    # 5) Attach handlers to ROOT
    root.addHandler(console)
    root.addHandler(file)


def main():
    setup_logging()

    # __name__ here is "__main__" (since we run this file directly)
    logger = logging.getLogger(__name__)
    logger.info("Program started.")

    utils.multiply(3, 4)
    utils.multiply(10, -5)

    logger.info("Program finished.")


if __name__ == "__main__":
    main()
