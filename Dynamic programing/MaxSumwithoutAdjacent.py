def Maxsum(arr):
    insum=0
    exsum=0
    for i in arr:
        insum1=insum
        insum=exsum+i
        exsum=insum1
    return max(insum,exsum)
print(Maxsum([5,10,10,100,5]))
