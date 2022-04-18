k=int(input("Enter a number"))
g=0
while(k!=1):
	if(k%4!=0):
		g=1
		print("this is not power of 4")
		break
	k=k/4
if(g==0):
	print("This is power of 4")