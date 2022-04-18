n=int(input("Enter a number"))
if((n!=0) and ((n&(n-1))==0) and not(n&0xAAAAAAAA)):
	print("This is power of 4")
else:
	print("This is not power of 4")