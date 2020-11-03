import numpy as nmp
from math import e
from pandas import DataFrame as  dfr

data=nmp.linspace(-1,1,19)
x_value=nmp.around(data,decimals=3)
count=(len(x_value))
table=nmp.zeros((count,count))
y_value=[]
for i in x_value:
    y_value.append(nmp.around((e**i),decimals=3))
table[:,0]=y_value
for i in range(1, count): 
    for j in range(count - i): 
        table[j][i] = nmp.around(table[j + 1][i - 1] - table[j][i - 1],3)
print(dfr(table,x_value,["y", "△y1", "△y2", "△y3", "△y4", "△y5", "△y6", "△y7", "△y8", "△y9", "△y10", "△y11", "△y12", "△y13", "△y14", "△y15", "△y16", "△y17", "△y18"]))
