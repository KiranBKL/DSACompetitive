def leaders(arr):
    leader=arr[-1]
    print(leader)
    for i in reversed(arr[:len(arr)-1]):
        if(i>leader):
            print(i)
            leader=i
leaders([7,10,4,10,3,6,5,2])
