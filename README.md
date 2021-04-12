# ML MODEL
This ML model computes whether there is a problem in a factory or not. It has 3 features: humidity, sound, and temperature. If there is a problem in the factory, sound will be greater than 85. I traind the model so that it recognizes this pattern by itself. 


## Commands (project run with WSL)

* Running the command: “MLFLOW_TRACKING_USERNAME=FLO MLFLOW_TRACKING_PASSWORD=SECRET  mlflow ui” will open the MLFlow Database on localhost:5000 

* The command “MLFLOW_TRACKING_USERNAME=FLO MLFLOW_TRACKING_PASSWORD=SECRET python3 model.py” will run the model and log the metrics to mlflow

* Running the Flask API with the following command (running on Linux): 
FLASK_DEBUG=1 FLASK_APP=flaskApi.py flask run --port=5001 


