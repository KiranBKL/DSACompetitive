def BinarySearch(arr,low,high,k):
	if(low<=high):
		mid=(low+high)//2
		print(low," ",mid," ",high,"\n")
		if(k<arr[mid]):
			high=mid-1
			return BinarySearch(arr,low,high,k)
		elif(k>arr[mid]):
			low=mid+1
			return BinarySearch(arr,low,high,k)
		else:
			return mid
	else:
		return "element not found"
print("Enter the length of the array")
n=int(input())
print("enter the elements")
arr=[]
for i in range(0,n):
	arr.append(int(input()))
arr.sort()
k=int(input("Enter element to search"))
print("element found at ",BinarySearch(arr,0,n-1,k))
