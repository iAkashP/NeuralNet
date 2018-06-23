import numpy as np
import sys
import matplotlib.pyplot as plt
x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7]
y=[0.15,0.3,0.37,0.45,0.6,0.7,0.9]
w=[0.5,0.5,0.5]
mew=0.1

plt.ion()
def out(x,w):
    s=[]
    for i in range(0,len(x)):
        s.append((w[0]*x[i]**2) + (w[1]*x[i])+(w[1]*1))
    return s

yt=out(x,w)
print(yt)
for i in xrange(10000):
    predict=out(x,w)
    for t in range(0,len(x)):
        w[0]=w[0]+mew*(y[t]-predict[t])*x[t]
        w[1]=w[1]+mew*(y[t]-predict[t])*1
    plt.clf()
    plt.scatter(x,y,c='red')
    predict=out(x,w)
    plt.plot(x,predict)
    plt.draw()
    plt.pause(0.01)


predict=out(x,w)
print(predict)
rs=0
for i in range(0,len(x)):
    rs=rs+((y[i]-predict[i])**2)
print(rs)
plt.show(block=True)
