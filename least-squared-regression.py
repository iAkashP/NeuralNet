import numpy as np
import matplotlib.pyplot as plt
import sys
x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7]
y=[0.2,0.43,0.61,0.756,0.8,0.84,0.95]

x_mean=np.mean(x)
y_mean=np.mean(y)
print(x_mean,y_mean)


least_square=sum((x-x_mean)**2)
numerator=sum((x-x_mean)*(y-y_mean))
print(least_square,numerator)

slope=numerator/least_square
intercept=(y_mean-(slope*x_mean))

plt.scatter(x,y,c='red')
yt=[]
for i in range(0,len(x)):
    yt.append(slope*x[i]+intercept)

r_square=sum((yt-y_mean)**2)/sum((y-y_mean)**2)
std_error=np.sqrt((sum(yt-y_mean)**2)/(len(x)-2))
print(yt)
print('R_Square: ',r_square)
print('Std_Error: ',std_error)
s=0
for i in range(0,len(x)):
    s=s+((y[i]-yt[i])**2)
print('Squared_Error: ',s)
plt.plot(x,yt)
plt.show()
