import numpy as np
def pairsum(ar,tar):
    l=0
    h=len(ar)-1
    arr=np.array(ar)
    while(l<h):
        s=arr[l]+arr[h]
        if(s==tar):
            return("Yes")
        elif(s>tar):
            h-=1
        else:
            l+=1
    return("No")
def tp(arr,tar):
    for i in range(len(arr)-2):
        if(pairsum(arr[i+1:],tar-arr[i]=="Yes")):
            return("yes")
    return("No")
print(tp([2,3,4,8,9,20,40],32))