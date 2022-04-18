def RemoveDup(arr):
    res=1
    for i in arr[1:]:
        if(i!=arr[res-1]):
            arr[res]=i
            res+=1
    print(arr[:res])
RemoveDup([10,20,20,30,30,30])