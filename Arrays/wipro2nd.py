n=int(input())
arr=input().split()
arr=[int(x) for x in arr]
#print(arr)
arr2=input().split(" ")
a,b=int(arr2[0]),int(arr2[1])
arr[a],arr[b]=arr[b],arr[a]
for i in arr:
    print(i,end=" ")