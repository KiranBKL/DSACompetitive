import numpy as np;
def CalculateSpan(arr):
    stack=[]
    stack.append(arr[0])
    s=np.zeros(shape=len(arr),dtype=int)
    s[0]=-1
    for i in range(1,len(arr)):
        while(len(stack)>0 and stack[-1]<=arr[i]):
            stack.pop()
        s[i]=-1 if(len(stack)<=0) else(stack[-1])
        stack.append(arr[i])
       # print(stack)
    print(s)
CalculateSpan([20,30,10,5,15])