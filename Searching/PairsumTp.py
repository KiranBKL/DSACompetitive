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
print(pairsum([2,5,8,12,30],17))