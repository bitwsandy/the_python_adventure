# task1_print_version.py
import logging

# Root logger setup
logging.basicConfig(
    level=logging.DEBUG,   # Change this later to DEBUG
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger()


def multiply(x, y):
    logger.debug("Starting multiplication...")

    result = x * y
    logger.info(f"Result of {x} * {y} is: {result}")

    logger.debug("Multiplication completed.\n")
    return result


multiply(3, 4)
multiply(10, -2)
