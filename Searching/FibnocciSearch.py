from bisect import bisect_left
def zonaccianSearch(arr, k, n):
	x = 0 # (m-2)'th Fibonacci No.
	y = 1 # (m-1)'th Fibonacci No.
	z = x + y # m'th Fibonacci

	while (z < n):
		x = y
		y = z
		z = x + y
	offset = -1

	while (z > 1):
		i = min(offset+x, n-1)
		print("x y z  offset arr[i]",x," ",y," ",z," ",offset," ",arr[i])

		if (arr[i] < k):
			z = y
			y = x
			x = z - y
			offset = i
			print("okkkkk")

		elif (arr[i] > k):
			z = x
			y = y - x
			x = z - y
			print(" not   okkkkk")

		else:
			return i

	if(y and arr[n-1] == x):
		return n-1

	return -1

arr = [10, 22, 35, 40, 45, 50,80, 82, 85, 90, 100,235]
n = len(arr)
x = 235
ind = zonaccianSearch(arr, x, n)
if ind>=0:
	print("Found at index:",ind)
else:
	print(x,"isn't present in the array");
