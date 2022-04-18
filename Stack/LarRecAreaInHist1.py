import numpy as np
def cal(arr):
    stack=[]
    stack.append(len(arr)-1)
    ns=np.zeros(shape=len(arr),dtype=int)
    ns[-1]=len(arr)
    for i in range(-2,-len(arr)-1,-1):
        while(len(stack)>0 and arr[stack[-1]]>=arr[i]):
            stack.pop()
        ns[i]=len(arr) if(len(stack)<=0) else(stack[-1])
        stack.append(i+len(arr))
    stack=[]
    stack.append(0)
    ps=np.zeros(shape=len(arr),dtype=int)
    ps[0]=-1
    for i in range(1,len(arr)):
        while(len(stack)>0 and arr[stack[-1]]>=arr[i]):
            stack.pop()
        ps[i]=-1 if(len(stack)<=0) else(stack[-1])
        stack.append(i)
    res=0
    print(ps)
    print(ns)
    for i in range(0,len(arr)):
        cur=arr[i]+arr[i]*(i-ps[i]-1)+arr[i]*(ns[i]-i-1)
       # print(f"{cur} {i}")
        res=max(res,cur)
    return res
    
print(cal([6,2,5,4,5,1,6]))

