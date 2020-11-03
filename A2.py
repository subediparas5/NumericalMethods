from math import exp
from pandas import DataFrame as dfr
def f(x):
    return exp(x) - 4*x
def df(x):
    return x*exp(x) - 4
def newtonRaphson(x):
    xList=[]
    yList=[]
    while True:
        xList.append(x)
        yList.append(f(x))
        if f(x) == 0.0:
            break
        x = x - f(x)/df(x)
    dframe=dfr()
    dframe["x"]=xList
    dframe["f(x)"]=yList
    print(dframe)
    print("The value of root is:", x)
x = 1.0
newtonRaphson(x)
