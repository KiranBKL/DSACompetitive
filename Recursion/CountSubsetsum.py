def countsubsetsum(arr,n,sum):
    if(n==0):
        if(sum==0):
            return 1
        return 0
    return countsubsetsum(arr,n-1,sum)+countsubsetsum(arr,n-1,sum-arr[n-1])

print(countsubsetsum([10,20,15],3,25))


