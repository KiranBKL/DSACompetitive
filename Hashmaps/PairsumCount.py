def countt(arr,k):
    s={}
    res=0
    for i in arr:
        s[i]=None
    for j in arr:
        if( (j+k) in s.keys()):
            res+=1
    print(res)
arr=[1,5,3,4,2]
countt(arr,2)
