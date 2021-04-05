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


reg.fit(X,y)
# coef tells us what kind of function it thinks is right. coeffient, because you multiply it with that.
print(reg.coef_)
# interef how much I add to the result
print(reg.intercept_)