# ML MODEL
This ML model computes whether there is a problem in a factory or not. It has 3 features: humidity, sound, and temperature. If there is a problem in the factory, sound will be greater than 85. I traind the model so that it recognizes this pattern by itself. 



Running the command: “MLFLOW_TRACKING_USERNAME=FLO MLFLOW_TRACKING_PASSWORD=SECRET  mlflow ui” will open the MLFlow Database on localhost:5000 

The command “MLFLOW_TRACKING_USERNAME=FLO MLFLOW_TRACKING_PASSWORD=SECRET python3 model.py” will run the model and log the metrics to mlflow

