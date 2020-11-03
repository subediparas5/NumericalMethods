import numpy as nmp
from pandas import DataFrame as dfr
import matplotlib.pyplot as plt 
def f(x, y):
    return x**2+x
xo = 0
yo = 1
intervals = nmp.linspace(0, 2, 21)
h = intervals[1] - intervals[0]
y = list()
y.append(yo)
for x in intervals[1:]:
    xo = x
    yi = y[-1] + h*f(xo, y[-1])
    y.append(yi)
df = dfr()
df["xi"]= intervals
df["yi"] = y
print(df)
plt.plot(intervals, y)
plt.title("Euler method plot of dy/dx=x^2+x")
plt.show()
