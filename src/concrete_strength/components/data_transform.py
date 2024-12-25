import os 
import sys 
from src.concrete_strength.exception import CustomException
from src.concrete_strength.logger import logging
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
import pandas as  pd 
import numpy as np 
from src.concrete_strength.utils import save_object

@dataclass
class DataTransformerConfig:
    preprocessor_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformer:
    def __init__(self):
        self.data_transformation_config = DataTransformerConfig()

    def get_data_transform_object(self):

        try:

            data_columns = ['cement', 'blast_furnace_slag', 'fly_ash', 'water', 'superplasticizer',
       'coarse_aggregate', 'fine_aggregate', 'age']
            
            pipeline = Pipeline(steps=[
                ('StandardScaler',StandardScaler()),
                ('Imputer',SimpleImputer(strategy='median'))
            ])

            preprocessor = ColumnTransformer([
                ('preprocess',pipeline,data_columns)
            ])

            return preprocessor

        except Exception as e :
            raise CustomException(e,sys)
        

    def initiate_data_transformation(self,train_path,test_path):
        try:
            logging.info("Data Transfoemation started")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            preprocess_obj = self.get_data_transform_object()

            target_column = 'concrete_compressive_strength'

            input_feature_train_df = train_df.drop(target_column,axis=1)
            target_feature_train_df = train_df[target_column]

            input_feature_test_df = test_df.drop(target_column,axis= 1)
            target_feature_test_df = test_df[target_column]

            logging.info("Applying preprocessing on train and test data")

            input_feature_train_arr = preprocess_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocess_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info("Save preprocess object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_file_path,
                obj = preprocess_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_file_path
            )
        except Exception as e :
            raise CustomException(e,sys)