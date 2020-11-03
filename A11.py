import numpy as nmp
import math
def estimate(x_predicted):
    x = nmp.array([1, 2, 3, 4, 5, 6])
    y = nmp.array([2.4, 3.1, 3.5, 4.2, 5.0, 6.0])
    a1 = len(x)
    b1 = x.sum()
    c1 = y.sum()
    a2 = x.sum()
    b2 = sum(x**2)
    c2 = sum(x*y)
    A = nmp.array([[a1, b1],
    [a2, b2]])
    b = nmp.array([c1, c2])
    a0, a1 = nmp.linalg.solve(A, b)
    y=a0 + (a1 * x_predicted)
    print("At x=2.5, y=",y)
estimate(x_predicted=2.5)
