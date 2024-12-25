
from src.concrete_strength.exception import CustomException
from src.concrete_strength.logger import logging
import sys
from src.concrete_strength.components.data_ingestion import DataIngestion
from src.concrete_strength.components.data_transform import DataTransformer


if __name__ == "__main__":
    data= DataIngestion()
    train_path,test_path = data.initiate_data_ingestion()

    transform_data = DataTransformer()
    transform_data.initiate_data_transformation(train_path,test_path)