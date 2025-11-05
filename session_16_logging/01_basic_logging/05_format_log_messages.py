import logging

logging.basicConfig(
    level=logging.DEBUG,
    format=(
        "%(asctime)s | %(levelname)s | %(name)s | "
        "%(filename)s:%(lineno)d %(funcName)s() | %(message)s"
    )
)

def calculate(x, y):
    logging.debug("adding numbers")
    return x + y

logging.info("starting calc")
result = calculate(2, 3)
logging.info("result = %s", result)
