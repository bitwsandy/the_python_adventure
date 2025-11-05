import logging

# Resetting basicConfig in the same process is tricky; run this in a fresh Python session.
logging.basicConfig(
    level=logging.DEBUG,  # now DEBUG and above will emit
    format="%(levelname)s | %(name)s | %(message)s"
)

logging.debug("now DEBUG is visible")
logging.info("INFO is visible too")
logging.warning("WARNING is visible")
