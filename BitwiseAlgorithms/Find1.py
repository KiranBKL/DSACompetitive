# Python3 code to find the element
# that occur only once
INT_SIZE = 32

def getSingle(arr, n) :
	
	# Initialize result
	result = 0
	
	# Iterate through every bit
	for i in range(0, INT_SIZE) :
		
		# Find sum of set bits
		# at ith position in all
		# array elements
		sm = 0
		x = (1 << i)
		print("\n",x,"\n")
		for j in range(0, n) :
			print(arr[j] & x)
			if (arr[j] & x) :
				sm = sm + 1
				
		# The bits with sum not
		# multiple of 3, are the
		# bits of element with
		# single occurrence.
		if ((sm % 3)!= 0) :
			result = result | x
	
	return result
	
# Driver program
arr = [3,3,2,3]
n = len(arr)
print("The element with single occurrence is ", getSingle(arr, n))


# This code is contributed
# by Nikita Tiwari.
