# utils.py
import logging

"""
No configuration here. Just get a module logger.
__name__ resolves to "utils" (or "package.utils" if inside a package).
It inherits handlers/format from the ROOT logger configured in main.py.
"""
logger = logging.getLogger(__name__)

def multiply(x, y):
    logger.info("Starting multiplication...")
    logger.debug("Inputs: x=%s, y=%s", x, y)     # Visible only in file (DEBUG+)

    result = x * y
    logger.info("Result of %s * %s = %s", x, y, result)

    if result < 0:
        logger.warning("Negative result detected → check inputs.")

    logger.info("Multiplication completed.\n")
    return result
