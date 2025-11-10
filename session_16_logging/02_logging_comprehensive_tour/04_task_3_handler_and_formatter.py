import logging

"""
-----------------------------------------------------------
LOGGING – FOUNDATIONAL CONCEPTS DEMO
-----------------------------------------------------------
In logging, three main components work together:

1) Logger      → Creates log messages.
2) Handler     → Decides WHERE the log should go (console/file/etc).
3) Formatter   → Decides HOW the log message looks.

Flow: logger → formatter → handler → output
-----------------------------------------------------------
"""

# 1. Create a Logger
# Name helps identify where logs came from (useful in multi-file apps).
logger = logging.getLogger("my_app")

# Set the minimum severity level the logger will accept.
# If a message is below this level → it will be ignored.
logger.setLevel(logging.INFO)   # Allows INFO, WARNING, ERROR, CRITICAL


# 2. Create a Handler
# StreamHandler sends logs to the console (terminal).
console_handler = logging.StreamHandler()


# 3. Create a Formatter
# Controls the appearance/format of log messages.
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


# 4. Attach the formatter to the handler
console_handler.setFormatter(formatter)


# 5. Attach the handler to the logger
logger.addHandler(console_handler)


# ----------------------------------------------------------
# Example function using logger instead of print()
# ----------------------------------------------------------

def multiply(x, y):
    # Informational progress messages
    logger.info("Starting multiplication...")

    # Internal debugging information (will show only if level = DEBUG)
    logger.debug("multiply() called with x=%s, y=%s", x, y)

    result = x * y

    # Info-level result
    logger.info("Result of %s * %s = %s", x, y, result)

    # Just demonstrating that we can log warnings/errors too:
    if result < 0:
        logger.warning("Result is negative. Check input values.")

    logger.info("Multiplication completed.\n")

    return result


# ----------------------------------------------------------
# Function Calls
# ----------------------------------------------------------
multiply(3, 4)
multiply(7, -5)


# Notes :
#
# | Concept                 | Meaning                                                      |
# | ----------------------- | ------------------------------------------------------------ |
# | Logger              | Component that *creates* log messages (`logging.getLogger`)  |
# | Handler             | Sends logs to console/file/etc (`StreamHandler`)             |
# | Formatter          | Controls log message layout (`%(levelname)s`, `%(message)s`) |
# | setLevel()          | Controls which log levels appear                             |
# | logger.addHandler() | Connects logger → handler → output
#
#
# logger.info("Message")        # Produces the log
#          │
#          ▼
# formatter (changes text)
#          │
#          ▼
# handler (decides where to send logs)
#          │
#          ▼
# console / file / cloud|
