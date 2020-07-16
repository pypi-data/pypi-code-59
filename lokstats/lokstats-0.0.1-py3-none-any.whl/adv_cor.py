"""
Created on Thu Jul 16 13:58:04 2020

@author: LOKSUNDAR
"""
import pandas as pd
import numpy as np
import numpy.linalg as mat
def partcor(df,a,b):
    x=list(df.columns)
    covmat=df.cov()
    s11=np.cov(df[a],df[b])
    df1=df.drop([a,b],axis=1)
    y=list(df1.columns)
    s12=np.zeros([2,len(y)])
    j=0
    for i in y:
        s12[0][j]=np.cov(df[a],df[i])[0][1]
        j=j+1
    j=0
    for i in y:
        s12[1][j]=np.cov(df[b],df[i])[0][1]
        j=j+1
    s21=np.zeros([len(y),2])
    j=0
    for i in y:
        s21[j][0]=np.cov(df[i],df[a])[0][1]
        s21[j][1]=np.cov(df[i],df[b])[0][1]
        j=j+1
    s22=df1.cov().to_numpy()
    fmat = s11-s12@(mat.inv(s22))@s21
    pc = fmat[0,1]/(np.sqrt(fmat[0,0]*fmat[1,1]))
    return pc
def mulcor(df,a):
    s11 = df.cov()[a][a]
    s1t = df.cov()[a]
    s1t=s1t.drop(a,axis=0).to_numpy()
    s1 = np.transpose(s1t).reshape(len(s1t),1)
    df1 = df.drop(a,axis=1)  
    s22 = df1.cov().to_numpy()
    val = np.sqrt((s1t@(mat.inv(s22))@s1)/s11)
    return val