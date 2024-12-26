from src.concrete_strength.components.data_ingestion import DataIngestion
from src.concrete_strength.components.data_transform import DataTransformer
from src.concrete_strength.components.model_trainer import MOdelTrainer



if __name__ == "__main__":
    data_ingestion = DataIngestion()
    train_path,test_path =  data_ingestion.initiate_data_ingestion()

    data_transform = DataTransformer()
    train_arr,test_arr,_ = data_transform.initiate_data_transformation(train_path,test_path)

    model_train = MOdelTrainer()
    model_train.initiate_model_training(train_arr,test_arr)