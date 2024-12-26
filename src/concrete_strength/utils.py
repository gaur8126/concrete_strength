import os 
import sys 
import pickle
from src.concrete_strength.exception import CustomException
from src.concrete_strength.logger import logging
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path , exist_ok=True)

        with open(file_path,'wb') as obj_file:
            pickle.dump(obj,obj_file) 
    except Exception as e :
        raise CustomException(e,sys)
    

def evaluate_model(x_train,y_train,x_test,y_test,models,params):

    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = params[list(params.keys())[i]]
            gs = GridSearchCV(model,param_grid=para,cv=3)
            gs.fit(x_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)

            y_pred = model.predict(x_test)

            score = r2_score(y_test,y_pred)
            report[list(params.keys())[i]] = score

        return report 
    
    except Exception as e:
        raise CustomException(e,sys)


def load_obj(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e :
        raise CustomException(e,sys)