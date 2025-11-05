
import logging

logging.basicConfig(
    level=logging.CRITICAL # now DEBUG and above will emit
)

def do_work_log():
    logging.warning("starting work")   # comparable visibility to print
    logging.info("processing...")      # lower level than WARNING
    logging.error("done")
    logging.debug("SUCCESS")

do_work_log()  # you'll only see WARNING/ERROR until you change the level (next steps)