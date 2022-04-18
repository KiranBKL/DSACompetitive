import numpy as np
def Maxsum(arr):
    arr1=np.array(arr)
    res=arr1[0]
    maxending=arr1[0]
    for i in arr1[1:]:
        maxending=max(maxending+i,i)
        res=max(res,maxending)
    return res
print(Maxsum([-3,8,-2,4,-5,6]))