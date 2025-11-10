import logging

# Root logger setup
logging.basicConfig(
    level=logging.INFO,   # Change this later to DEBUG
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger()

def multiply(x, y):
    logger.debug("multiply() called with x=%s, y=%s", x, y)  # DEBUG (Usually hidden)
    logger.info("Starting multiplication...")                # INFO (Visible at INFO level)

    result = x * y

    logger.debug("Raw result calculated: %s", result)        # DEBUG (Hidden unless DEBUG)
    logger.info("Final result of %s * %s = %s", x, y, result)

    return result


multiply(5, 6)
multiply(-2, 8)


# | Level      | Meaning                                    | When Used            | Visible at Level                      |
# | ---------- | ------------------------------------------ | -------------------- | ------------------------------------- |
# | `DEBUG`    | Developer internal messages                | deep troubleshooting | Only when logging level = DEBUG       |
# | `INFO`     | Normal program steps                       | progress messages    | INFO + DEBUG levels                   |
# | `WARNING`  | Something unexpected but program continues | caution              | always shown (unless level is ERROR+) |
# | `ERROR`    | Program failed                             | errors               | always shown                          |
# | `CRITICAL` | Serious failure                            | system crash level   | always shown                          |
