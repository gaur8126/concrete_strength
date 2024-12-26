import os 
import sys 
import pandas  as pd 
import numpy as np 
from src.concrete_strength.exception import CustomException
from src.concrete_strength.logger import logging
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor,RandomForestRegressor,GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm  import SVR
from xgboost import XGBRFRegressor
from catboost import CatBoostRegressor
from dataclasses import dataclass
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from src.concrete_strength.utils import evaluate_model,save_object

@dataclass
class ModelTrainerConfig:
    training_file_path= os.path.join('artifacts','model.pkl')

class MOdelTrainer:
    def __init__(self):
        self.trainer_config = ModelTrainerConfig()

    def eval_matrics(self,actual,predicted):
        mae = mean_absolute_error(actual,predicted)
        rmse = np.sqrt(mean_squared_error(actual,predicted))
        r2_square = r2_score(actual,predicted)
        return mae,rmse,r2_square

    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info("train test split")

            x_train,y_train,x_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            ) 

            logging.info("Model training start")

            models = {
                "LinearRegressor":LinearRegression(),
                "DecisionTree":DecisionTreeRegressor(),
                "AdaBoostRegressor":AdaBoostRegressor(),
                "RandomForestRegressor":RandomForestRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "KNeighborsRegressor":KNeighborsRegressor(),
                "SVR":SVR(),
                # "XGBRFRegressor":XGBRFRegressor(),
                "CatBoostRegressor":CatBoostRegressor()

            }

            params = {
                "LinearRegressor":{},
                "DecisionTree":{
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    'splitter':['best',"random"],
                    'max_depth':[1,3,5,7],
                    'max_features':['sqrt','log2']
                },
                "AdaBoostRegressor":{
                    'learning_rate':[0.001,0.01,1,1.01],
                    'loss':['linear','square', 'exponential']
                },
                "RandomForestRegressor":{
                    'criterion':['squared_error', 'absolute_error', 'friedman_mse', 'poisson'],
                    'max_depth':[1,3,5,7],
                    'max_features':['sqrt','log2']
                },
                "GradientBoostingRegressor":{
                    'loss':['squared_error', 'absolute_error', 'huber', 'quantile'],  
                    'criterion':['friedman_mse', 'squared_error'],
                 },
                 "KNeighborsRegressor":{
                     'n_neighbors':[3,5,7,9],
                     'weights':['uniform','distance'],
                     'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute']
                 },
                 'SVR':{
                    #  'loss':['epsilon_insensitive','squared_epsilon_insensitive'],

                 },
                #  "XGBRFRegressor":{
                #      "booster":['gbtree', 'gblinear' ,'dart'],
                #      "learning_rate":[0.001,0.01,0.1]
                #  },
                 "CatBoostRegressor":{
                    #  "learning_rate":[0.001,0.01,0.1],
                    #  "bootstrap_type":["Bayesian", "Bernoulli", "MVS"],
                    #  "loss_function":["RMSE", "MAE", "MAPE"]
                 }

            }

            model_report:dir = evaluate_model(x_train,y_train,x_test,y_test,models,params)
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            print(f"best model : {best_model}")
            print(f"best model score : {best_model_score}")

            model_name = list(params.keys())

            actula_model = ""

            for model in model_name :
                if best_model_name == model:
                    actula_model  = actula_model+model

            best_param = params[actula_model]

            print(f"best param {best_param}")

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info("best model found on test ans traini set ")

            
            save_object(
                self.trainer_config.training_file_path,
                obj = best_model
            )

            y_pred = best_model.predict(x_test)
            r2_square  = r2_score(y_test,y_pred)

            return r2_square

        except Exception as e:
            raise CustomException(e,sys)

