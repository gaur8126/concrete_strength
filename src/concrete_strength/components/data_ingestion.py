import pandas as pd 
import numpy as np 
import os 
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.concrete_strength.exception import CustomException
from src.concrete_strength.logger import logging




@dataclass
class DataIngestionConfig:
    train_data__path:str  = os.path.join('artifacts','train.csv')
    test_data__path :str = os.path.join('artifacts','test.csv')
    raw_data__path :str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.initiate_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info('Data Ingestion started')
            
            df = pd.read_csv(os.path.join('notebook/data','concrete_strength.csv'),index_col=0)
            os.makedirs(os.path.dirname(self.initiate_config.train_data__path),exist_ok=True)
            df.to_csv(self.initiate_config.raw_data__path,index=False,header=True)
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.initiate_config.train_data__path,index=False,header=True)
            test_set.to_csv(self.initiate_config.test_data__path,index=False,header = True)

            logging.info("Data Ingestion is comleted")

            return (
                self.initiate_config.train_data__path,
                self.initiate_config.test_data__path
            )
        except Exception as e:
            raise CustomException(e,sys)
