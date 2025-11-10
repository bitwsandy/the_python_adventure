# main.py
import logging
import utils   # we will call functions from this module

"""
------------------------------------------------------------
We configure logging ONCE in the entry point (main.py).

We configure the ROOT logger, so ALL other loggers
(e.g., utils, controllers, db) will automatically inherit
this configuration.

This is the simplest and most common real-world pattern.
------------------------------------------------------------
"""

# Configure ROOT logger
logging.basicConfig(
    level=logging.DEBUG,   # root logger will show INFO and above
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
# No handlers added manually here → basicConfig creates console handler.


def main():
    logger = logging.getLogger(__name__)   # This becomes "__main__"
    logger.info("Program started.")

    utils.multiply(3, 4)
    utils.multiply(10, -5)

    logger.info("Program finished.")


if __name__ == "__main__":
    main()
