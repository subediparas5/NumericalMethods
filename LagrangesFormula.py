xp = 2
x = [0,1,3,4,5]
y = [0,1,81,256,625]
yp = 0
for i in range(5):
    p = 1
    for j in range(5):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]
print('y(2)= %.4f.' % (yp))    
