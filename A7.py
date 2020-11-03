from math import exp, pi, sqrt
import numpy as nmp

intervals = nmp.linspace(-4, 4, 51)
h = intervals[1] - intervals[0]
y = list()
for i in intervals:
    y.append(sqrt(1/(2*pi)) * exp(i**2/2))
oddSum = nmp.sum(y[1:-1:2])
evenSum = nmp.sum(y[2:-1:2])
I = (h/3)*(y[0]+y[-1]+4*oddSum+2*evenSum)
print("I=%.5f"%(I))
