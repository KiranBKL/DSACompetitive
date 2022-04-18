import numpy as np;
def CalculateSpan(arr):
    stack=[]
    stack.append(0)
    s=np.zeros(shape=len(arr),dtype=int)
    s[0]=1
    for i in range(1,len(arr)):
        while(len(stack)>0 and arr[stack[-1]]<=arr[i]):
            stack.pop()
        s[i]=i+1 if(len(stack)<=0) else(i-stack[-1])
        stack.append(i)
    print(s)
CalculateSpan([13,15,12,14,16,8,6,4,10,30])