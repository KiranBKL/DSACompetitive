import numpy as np
def WindowSum(a,k):
    arr=np.array(a)
    res=sum(arr[:k])
    #print(res)
    cursum=res
    for i in range(k,len(arr)):
        cursum=cursum+arr[i]-arr[i-k]
        res=max(res,cursum)
     #   print(cursum)
    print(res)
WindowSum([1,8,30,-5,20,7],3)