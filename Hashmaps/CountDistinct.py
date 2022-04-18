def CDE(arr):
    s={}
    for i in arr:
        if(i not in s.keys()):
            s[i]=None
    print(len(s))
arr=[10,20,10,20,30]
CDE(arr)
