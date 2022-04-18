print("Enter the length of the array")
n=int(input())
print("enter the elements")
arr=[]
for i in range(0,n):
	arr.append(int(input()))
k=int(input("Enter element to search"))
for i in arr:
	if(i==k):
		print("element found")
