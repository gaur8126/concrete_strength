
from src.concrete_strength.exception import CustomException
from src.concrete_strength.logger import logging
import sys




if __name__ == "__main__":
    logging.info("Execusion has started")
    try :
        1/0
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)
