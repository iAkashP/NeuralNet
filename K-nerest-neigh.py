import numpy as np
import pandas as pd
import time

df=pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?',-999999,inplace=True)
df.drop(['id'],1,inplace=True)
X=np.array(df.drop(['class'],1),dtype=float)
y=np.array(df['class'])
yt=[5,1,1,1,2,1,3,1,1]
clss=[2,4]

def euclid_dist(X,yt):
    fr=(np.shape(X))
    dist=np.zeros((fr[0],1))
    for i in range(0,fr[0]):
        rt=(X[i]-yt)**2
        euc=(np.sqrt(np.sum(rt)))
        dist[i]=euc
    return dist,np.argsort(dist,axis=0)

def classifier_knearest(X,y,yt,k,clss):
    dist,index=euclid_dist(X,yt)
    clss_temp=np.zeros((1,k))
    for i in xrange(k):
        ind=index[k]
        clss_temp[0][i]=y[ind][0]
    clss_predict=[]
    for i in xrange(len(clss)):
        clss_predict.append(np.count_nonzero(clss_temp == clss[i]))
    index_max = max(xrange(len(clss_predict)), key=clss_predict.__getitem__)
    return (clss[index_max])


# dist,index=euclid_dist(X,yt)
clss_tmp=classifier_knearest(X,y,yt,3,clss)
print(clss_tmp)
