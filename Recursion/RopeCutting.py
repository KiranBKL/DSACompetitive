def ropeCut(n):
    if(n==0):
        return 0
    if(n<0):
        return -1
    res=max(ropeCut(n-11),max(ropeCut(n-9),ropeCut(n-12)))
    if(n==-1):
        return -1
    return res+1
print(ropeCut(81))


