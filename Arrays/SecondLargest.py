def secondLast(arr):
    res=-1
    lar=0
    for i in range(1,len(arr)):
        if(arr[i]>arr[lar]):
            res=lar
            lar=i
        elif(arr[i]!=arr[lar]):
            if(res==-1 or arr[i]>arr[res]):
                res=i
    return res