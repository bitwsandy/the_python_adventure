import logging

"""
-----------------------------------------------------------
LOGGING WITH MULTIPLE HANDLERS (Console + File)
-----------------------------------------------------------
We will extend the previous script:

Logger → ConsoleHandler      → Shows logs on screen
       → FileHandler         → Writes logs into app.log file

Both handlers can share the same formatter (common format).
-----------------------------------------------------------
"""


# 1. Create the logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)   # Logger will accept INFO and above


# 2. Create a Console Handler
console_handler = logging.StreamHandler()


# 3. Create a File Handler (logs will be stored in app.log)
file_handler = logging.FileHandler("app.log")   # Creates file if not present


# 4. Create a common Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# 5. Attach formatter to both handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


# 6. Attach handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# ----------------------------------------------------------
# Example function using the logger
# ----------------------------------------------------------

def multiply(x, y):
    logger.info("Starting multiplication...")
    result = x * y

    logger.info("Result of %s * %s = %s", x, y, result)

    if result < 0:
        logger.warning("Result is negative. Check input values.")

    logger.info("Multiplication completed.\n")
    return result


# ----------------------------------------------------------
# Run the function
# ----------------------------------------------------------
multiply(4, 5)
multiply(10, -3)



# | Component                 | Description                                              |
# | ------------------------- | -------------------------------------------------------- |
# | FileHandler           | Writes logs to a file                                    |
# | Multiple Handlers    | Logger can output logs to multiple places simultaneously |
# | Same formatter reused | Ensures consistent log formatting everywhere             |
