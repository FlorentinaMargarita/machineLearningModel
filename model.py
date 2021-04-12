from sklearn import linear_model
import sklearn.metrics
from mlflow import log_metric, log_param, log_artifacts
import mlflow.sklearn
import mlflow

# Instead of sending its information directly to the MLrun directory, model.py will send its information to the MLflow server  
# Thereby it tries to make an http connection to localhost 80 instead of directly writing to MLruns. In order for it to get through the NGINX 
# security layer, the user needs to pass it a password and a user name.
mlflow.set_tracking_uri('http://localhost')

# "with" is there for autolog and log_metric to run at the same time
with mlflow.start_run(): 

  mlflow.sklearn.autolog(exclusive=False)

  reg = linear_model.LinearRegression(fit_intercept=True)

  f = open("data", "r")

  # final matrix
  X = []
  y = []

  for x in f:
  #  this will store each element of the array in one of those four variables
    t,h,s,p = x.split(" ")
  #   fit wants integers so I convert it into integers
    t = int(t)
    h = int(h)
    s = int(s)
    p = int(p)

    X.append([t,h,s])
    y.append(p)

  # fit is the learning, training part. this is were it learns all the data and runs the regression
  reg.fit(X,y)
  # coef tells us what kind of function it thinks is right. coeffient, because you multiply it with that.
  # here it prints out the parameters (reg.coef_, reg.intercept_) of the model that it learnt with reg.fit()
  print(reg.coef_)
  # intercept: This value is added to result (represent point where the function crosses the y-axis)
  print(reg.intercept_)


  # here comes the test part
  # predict is a function using data from the test data file, which I also generated using generate.py>test.
  f = open("test", "r")

  # final matrix
  XTEST= []
  ytest = []

  for x in f:
  #  this will store each element of the array in one of those four variables
    t,h,s,p = x.split(" ")
  #   fit wants integers so I convert them into integers
    t = int(t)
    h = int(h)
    s = int(s)
    p = int(p)


    XTEST.append([t,h,s])
    ytest.append(p)

  # coef and intercept don't change anymore. They are set on what they are. 
  # The sensor data is in XTEST and I pass it to predict.
  # Predict then predicts which of the data points are a problem or are not a problem.
  prediction = reg.predict(XTEST)

  # answerArray gets all real predictions
  answerArray = []

  # pred is one value in the test data set. Multiplied by the coefs and added intercepts. 
  # (temperature * coef[0] + humidity * coef[1] + sound * coef[2]) + intercept = result is <0.5< . 
  # I don't round in case there is a number bigger than 1, that I will still get a result which is either 0 or 1. 
  for pred in prediction: 
      if pred > 0.5: answerArray.append(1)
      else: answerArray.append(0)

  # the first argument is the answer, I know is correct. the second argument is the predicted one.
  # this r^2 that is coeffient of determination. 
  # 1 is a perfect correlation between line and points. 0 means there is no correlation between line and points. 
  log_metric("R2 METRIC", sklearn.metrics.r2_score(ytest, answerArray))
  # The closer to 0 the better. In this case the worst would be 1.
  log_metric("mean squared error", sklearn.metrics.mean_squared_error(ytest, answerArray))
  # this is the mean (average) absolute error. (by mulitplying it with the length of the correct answers array, I would get the total absolute error.)
  log_metric("mean absolute error", sklearn.metrics.mean_absolute_error(ytest, answerArray))