import math
def JumpSearch(arr,k,n):
	step=int(math.sqrt(n))
	incr=int(math.sqrt(n))
	prev=0
	print("\n\n",k,"\n")
	print("prev step incr arr[min(step,n)-1]",prev," ",step," ",incr," ",arr[min(step,n)-1])
	while arr[min(step,n)-1] < k:
		prev=step
		step=step+incr
		print("prev step incr arr[min(step,n)-1]",prev," ",step," ",incr," ",arr[min(step,n)-1])
		if(prev>=n):
			return -1
	while arr[prev]<k:
		prev+=1
		print("prev step incr",prev," ",step," ",incr)
		if prev == min(step,n):
			return -1
	if(arr[prev]==k):
		return prev
	return -1

print("Enter the length of the array")
n=int(input())
print("enter the elements")
arr=[]
for i in range(0,n):
	arr.append(int(input()))
arr.sort()
for k in arr:
	print("element found at",JumpSearch(arr,k,n),"/n/n/n")

k=int(input("Enter element to search"))
print("element found at",JumpSearch(arr,k,n))