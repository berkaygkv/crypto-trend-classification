# Crypto Trend Prediction Algorithm
This is an __MLflow__ integrated pipeline built using __Ploomber__ framework. Upon providing the required list of parameters, the input data will be processed and fed into the __XGBoost Classifier__ which will be trained to predict in binary sense whether a given set of financials is neutral or bullish/bearish (e.g., it has reached the local maxima or minima). 

The code itself can download the requested Crypto through using binance client (of which you'll need an API key provided in a keys.yaml file). This project in on development phase. Hopefully I will be fixing some bugs and adding the multiclass version of the work.

__**DISCLAIMER: This algorithm is built for learning purposes and it's NOT advised to use it on live trading**__


## First Experiment Notebook
You can access the very first notebook output of the pipeline here: [Notebook: report-0](products/notebooks/report-0.ipynb)


## MLFlow View
![Alt Text](img/mlflow.gif)
