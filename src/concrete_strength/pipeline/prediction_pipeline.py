import os 
import sys 
import pandas as pd 
import numpy as np 
from src.concrete_strength.exception import CustomException
from src.concrete_strength.logger import logging
from src.concrete_strength.utils import load_obj

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path = "artifacts/preprocessor.pkl" #os.path.join('artifacts','prerocessor.pkl')
            model_path =    "artifacts/model.pkl"                                  #os.path.join('artifacts','model.pkl')
            print("before loading")
            preprocessor = load_obj(file_path=preprocessor_path)
            model  = load_obj(file_path=model_path)
            print("after loading")
            datascaled = preprocessor.transform(features)
            pred = model.predict(datascaled)

            return pred
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:

    def __init__(self,
                        cement:float,
                        blast_furnace_slag:float,
                        fly_ash:float,
                        water:float,
                        superplasticizer:float,
                        coarse_aggregate:float,
                        fine_aggregate:float,
                        age:float):
        self.cement = cement
        self.blast_furnace_slag = blast_furnace_slag
        self.fly_ash = fly_ash
        self.water = water
        self.superplasticizer = superplasticizer
        self.coarse_aggregate = coarse_aggregate
        self.fine_aggregate = fine_aggregate
        self.age = age

    def get_dataframe(self):
        try:
            custom_data_input = {
            
            'cement':[self.cement],
            'blast_furnace_slag':[self.blast_furnace_slag],
            'fly_ash':[self.fly_ash], 
            'water':[self.water], 
            'superplasticizer':[self.superplasticizer],
            'coarse_aggregate':[self.coarse_aggregate], 
            'fine_aggregate':[self.fine_aggregate], 
            'age':[self.age] }

            logging.info("DataFrame Gathered")
            return pd.DataFrame(custom_data_input)
            
            
        except Exception as e:
            raise CustomException(e,sys)
