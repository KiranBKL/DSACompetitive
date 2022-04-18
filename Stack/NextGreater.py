import numpy as np;
def CalculateSpan(arr):
    stack=[]
    stack.append(arr[-1])
    s=np.zeros(shape=len(arr),dtype=int)
    s[-1]=-1
    for i in range(-2,-len(arr)-1,-1):
        while(len(stack)>0 and stack[-1]<=arr[i]):
            stack.pop()
        s[i]=-1 if(len(stack)<=0) else(stack[-1])
        stack.append(arr[i])
       # print(stack)
    print(s)
CalculateSpan([5,15,10,8,6,12,9,18])