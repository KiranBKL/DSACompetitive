 #import math as m
print("Enter the length of the array")
n=int(input())
print("enter the elements")
arr=[]
for i in range(0,n):
	arr.append(int(input()))
arr.sort()
#k=int(input("Enter element to search"))
for k in arr:
	print("\n\n\n",k,"\n\n")
	low=0
	high=n-1
	while(high>=low):
		mid=(low+high)//2
		print(low," ",mid," ",high,"\n")
		if(k<arr[mid]):
			high=mid-1
		elif(k>arr[mid]):
			low=mid+1
		else:
			print("element found at ",mid)
			break
	if(low>high):
		print("element not found")