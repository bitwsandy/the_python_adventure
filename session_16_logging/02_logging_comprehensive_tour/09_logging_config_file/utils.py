# utils.py
import logging

# __name__ resolves to "utils" → matches logger defined in logging.yaml
logger = logging.getLogger(__name__)

def multiply(x, y):
    logger.info("Starting multiplication...")
    logger.debug("Inputs: x=%s, y=%s", x, y)   # DEBUG shows in file
    result = x * y

    if result < 0:
        logger.warning("Negative result detected.")

    logger.info("Result: %s\n", result)
    return result
