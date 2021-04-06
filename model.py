from sklearn import linear_model

reg = linear_model.LinearRegression()

# reg.fit: two arguments to reg.fit(). First one is a matrix: This represents all the input values. 
# [0,0] are actually 

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
# here we print out the parameters (reg.coef_, reg.intercept_) of the model that it learnt with reg.fit()
print(reg.coef_)
# interef how much I add to the result
print(reg.intercept_)


# here comes the test part
# predict is a function. we will point it to a new data file => test, which I also generated using generate.py>test.

f = open("test", "r")

# final matrix
XTEST= []
ytest = []

for x in f:
#  this will store each element of the array in one of those four variables
  t,h,s,p = x.split(" ")
#   fit wants integers so I convert it into integers
  t = int(t)
  h = int(h)
  s = int(s)
  p = int(p)


  XTEST.append([t,h,s])
  ytest.append(p)

# coef and intercept doesn't change anymore. They are set on what they are. 
# The sensor data is in XTEST and I give it to predict.
# Predict then predicts which of the data points are problems or not.

prediction = reg.predict(XTEST)

# answerArray has all real predictions
answerArray = []

# pred is one value in the test data set. Multiplied by the coefs and added intercepts. 
# (temperature * coef[0] + humanity * coef[1] + sound * coef[2]) + intercept = result is <0.5< . 
# I don't round in case there is a number bigger than 1, that I will still get a result which is either 0 or 1 and 2.4 would round to 2. 

for pred in prediction: 
    if pred > 0.5: answerArray.append(1)
    else: answerArray.append(0)

residuals= []

# minimum absolute deviation (deviation in this case being the residuals) method 
for index in range(len(answerArray)):
  # abs = absolute value, so that -1 and +1 doesn't cancel out. 
  residuals.append(abs(ytest[index]-answerArray[index]))

print(sum(residuals), len(answerArray))