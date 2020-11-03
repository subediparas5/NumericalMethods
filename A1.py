from math import sin
from pandas import DataFrame as dfr
def f(x):return x**2 - sin(x)
lista=[]
listb=[]
listx0=[]
listfx0=[]
def table(a,b,c,d):
    lista.append(a)
    listb.append(b)
    listx0.append(c)
    listfx0.append(d)
def bisectionMethod(a, b):
    if f(a)*f(b) > 0.0:
        print("Choose alternate value of a and b.")
    else:
        while f(a)*f(b) < 0.0:
            c = (a+b)/2
            table(a,b,c,round(f(c),4))
            if f(c) == 0.0:
                break
            elif f(c)*f(a) < 0.0:
                b = c
            else:
                a = c
    print("The value of root is:", c)
a = 0.5
b = 1.0
bisectionMethod(a,b)
dfr = dfr()
dfr['a']=lista
dfr['b']=listb
dfr['x0']=listx0
dfr['f(x0)']=listfx0
print(dfr)
