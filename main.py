from _logging.logger import setup_logging, custom_logger
from app import app

setup_logging()
logger = custom_logger(__name__)

def main():
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("exception message")

if __name__ == '__main__':
    app()
    main()