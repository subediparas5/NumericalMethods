import numpy as nmp
 
n = int(input('Enter the no. of data: '))
x = nmp.zeros((n))
y = nmp.zeros((n,n))
print('Enter data')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1] 
print('\n--FORWARD DIFFERENCE TABLE--\n')
for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, n-i):
        print('\t\t%0.2f' %(y[i][j]), end='')
    print()
for i in range(1, 6):
    for j in range(6-1,i-2,-1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]    
print('\n--BACKWARD DIFFERENCE TABLE--\n')
for i in range(0,6):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, i+1):
        print('\t%0.2f' %(y[i][j]), end='')
    print()
