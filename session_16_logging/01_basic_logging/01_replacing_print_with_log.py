# # v1: prints
# def do_work_print():
#     print("starting work")
#     print("processing...")
#     print("done")
#
# do_work_print()

# v2: logging (drop-in replacement with richer context)
import logging

def do_work_log():
    logging.warning("starting work")   # comparable visibility to print
    logging.critical("processing...")      # lower level than WARNING
    logging.error("done")

do_work_log()  # you'll only see WARNING/ERROR until you change the level (next steps)
