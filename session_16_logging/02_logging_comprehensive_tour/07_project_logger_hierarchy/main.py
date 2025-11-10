# main.py
import logging
from logging import StreamHandler, FileHandler, Formatter
import utils

"""
Multi-module logging rules:

1) Configure logging ONLY in the program's entry point (here: main.py).
   - Handlers & formatter live here.
   - Avoid calling basicConfig() or adding handlers in imported modules.

2) In other modules (like utils.py), just create a named logger:
   logger = logging.getLogger(__name__)
   ...and log. Those logs "propagate" up to handlers defined here.
"""

def setup_logging():
    # Create top-level app logger (parent). You could also use "root".
    app_logger = logging.getLogger("app")
    app_logger.setLevel(logging.DEBUG)  # app accepts DEBUG and above

    # Console handler
    ch = StreamHandler()
    ch.setLevel(logging.INFO)  # console shows INFO+

    # File handler
    fh = FileHandler("app.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)  # file captures everything (DEBUG+)

    # Common formatter
    fmt = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(fmt)
    fh.setFormatter(fmt)

    # Attach handlers to app logger
    app_logger.addHandler(ch)
    app_logger.addHandler(fh)

    # Make module loggers flow into our app logger:
    # Map the root of our app ("app") to handle everything,
    # then set children to use names like "app.utils" below.
    #
    # Also: ensure the root logger doesn't add its own default handler noise.
    logging.getLogger().handlers.clear()

def main():
    setup_logging()

    # Create a child logger for main
    log = logging.getLogger("app.main")
    log.info("Program started.")

    # Rebind utils' logger to be a child of "app"
    # Easiest: rename utils' logger to "app.utils".
    # (We do it here to keep utils.py clean.)
    utils.logger = logging.getLogger("app.utils")

    # Now call utils (its logs propagate to "app" handlers)
    utils.multiply(4, 5)
    utils.multiply(7, -2)

    log.info("Program finished.")

if __name__ == "__main__":
    main()
