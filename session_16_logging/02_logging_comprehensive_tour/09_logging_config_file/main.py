# main.py
import logging.config
import yaml
import utils

def setup_logging():
    with open("logging.yaml", "r") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)

def main():
    setup_logging()

    logger = logging.getLogger(__name__)
    logger.info("Program started.")

    utils.multiply(6, 7)
    utils.multiply(-2, 9)

    logger.info("Program finished.")

if __name__ == "__main__":
    main()
