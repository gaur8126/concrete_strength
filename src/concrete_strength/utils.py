import os 
import sys 
import pickle
from src.concrete_strength.exception import CustomException
from src.concrete_strength.logger import logging

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path , exist_ok=True)

        with open(file_path,'wb') as obj_file:
            pickle.dump(obj,obj_file) 
    except Exception as e :
        raise CustomException(e,sys)