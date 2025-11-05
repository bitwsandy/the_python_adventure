import logging

# Fresh session recommended before re-calling basicConfig
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",              # write to file
    filemode="a",                    # overwrite on each run (use 'a' to append)
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s"
)
logging.info("this goes to app.log (not the console)")
logging.error("this too")

# # If you also want console output, add a StreamHandler:
# logger = logging.getLogger()  # root
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(logging.Formatter("%(levelname)s | %(message)s"))
# logger.addHandler(console)
#
# logging.info("now you see me in file AND console")
