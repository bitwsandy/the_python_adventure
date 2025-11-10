# utils.py
import logging

"""
------------------------------------------------------------
We do NOT configure logging here.
We simply obtain a logger for THIS module.

logging.getLogger(__name__) will produce a logger whose
name matches the module path:

main.py run directly      → "__main__"
utils.py when imported    → "utils"
package/utils.py          → "package.utils"

This automatically forms a meaningful hierarchy.
------------------------------------------------------------
"""

logger = logging.getLogger(__name__)   # This becomes "utils"


def multiply(x, y):
    logger.info("Starting multiplication...")
    logger.debug("Received x=%s, y=%s", x, y)  # DEBUG -> hidden unless root set to DEBUG

    result = x * y
    logger.info("Result of %s * %s = %s", x, y, result)

    if result < 0:
        logger.warning("Result is negative → check inputs.")

    logger.info("Multiplication completed.\n")
    return result
