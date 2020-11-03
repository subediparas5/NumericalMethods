import numpy as nmp
import math
def estimate(x_pred):
    x = nmp.array([2, 4, 6, 8, 10])
    y = nmp.array([4.077, 11.084, 30.128, 81.897, 222.62])
    a1 = len(x)
    b1 = x.sum()
    c1 = sum(nmp.log(y))
    a2 = x.sum()
    b2 = sum(x**2)
    c2 = sum(x*nmp.log(y))
    A = nmp.array([[a1, b1],[a2, b2]])
    b = nmp.array([c1, c2])
    a0, a1 = nmp.linalg.solve(A, b)
    print("At x=9, y=", nmp.exp(a0) * nmp.exp(a1 * x_pred))
estimate(9)
