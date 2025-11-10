# utils.py
import logging

# Create a module-specific (named) logger.
# Using __name__ results in "utils" when imported from main.py,
# or "package.utils" if this lived inside a package.
logger = logging.getLogger(__name__)  # "utils"

def multiply(x, y):
    logger.info("utils.multiply: starting ...")
    logger.debug("utils.multiply: received x=%s, y=%s", x, y)

    result = x * y

    if result < 0:
        logger.warning("utils.multiply: negative result detected: %s", result)

    logger.info("utils.multiply: finished → %s", result)
    return result
