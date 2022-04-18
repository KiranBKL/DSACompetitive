import numpy as np
def Rainwater(arr):
    n=len(arr)
    rain=np.array(arr)
    lmax=np.zeros(shape=n,dtype=int)
    rmax=np.zeros(shape=n,dtype=int)
    #print(rain.dtype)
    #rint(lmax.dtype)
    lmax[0]=rain[0]
    rmax[n-1]=rain[n-1]
    res=0
    for i in range(0,n):
        if(i==0):
            continue
        lmax[i]=max(rain[i],lmax[i-1])
        rmax[n-(i+1)]=max(rmax[n-i],rain[n-(i+1)])
    for i in range(1,n-1):
        res=res+(min(lmax[i],rmax[i])-rain[i])
    print(res)
Rainwater([5,0,6,2,3])
