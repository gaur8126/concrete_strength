from flask import Flask,render_template,request
from src.concrete_strength.pipeline.prediction_pipeline import PredictionPipeline,CustomData
import numpy as np 
import pandas as pd 

application = Flask(__name__)

app = application

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Create instance of CustomData
        # data = CustomData()
        
        # Use get_custom_data method to set the values
        data = CustomData(
            cement = float(request.form.get('cement')),
            blast_furnace_slag = float(request.form.get('blast_furnace_slag')),
            fly_ash = float(request.form.get('fly_ash')),
            water = float(request.form.get('water')),
            superplasticizer = float(request.form.get('superplasticizer')),
            coarse_aggregate = float(request.form.get('coarse_aggregate')),
            fine_aggregate = float(request.form.get('fine_aggregate')),
            age = float(request.form.get('age'))
        )

        # Get the dataframe and make prediction
        pred_df = data.get_dataframe()
        print(pred_df)
        predict_pipeline = PredictionPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=round(results[0],3))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)