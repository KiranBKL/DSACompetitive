from math import gcd

n=int(input())
arr=list(map(int,input().split()))
tar=int(input())
arr1=[0]*len(arr)
c=0
arr.sort()
for i in range(len(arr)):
	arr1[i]=arr[i]
inc=0
dec=0
def lcm(x,y):
	return x*y/(gcd(x,y))
for i in range(0,len(arr)-1):
	if(lcm(arr[i],arr[i+1])>tar):
		break
	for j in range(i+1,len(arr)):
		t=int(lcm(arr[i],arr[j]))
		#print(t)
		if(t<=tar):
			arr.append(t)
		else:
			break
#print(arr)
#print(arr1)
for i in range(len(arr)):
	if(i<len(arr1)):
		inc+=tar//arr1[i]
	else:
		dec+=tar//arr[i]
print(inc-dec)