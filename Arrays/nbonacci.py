import numpy as np
def bonacci(n,m):
    arr=np.zeros(shape=m,dtype=int)
    arr[n-1]=1
    for i in range(n,m):
        arr[i]=sum(arr[i-n:i])
    print(arr)
bonacci(3,8)