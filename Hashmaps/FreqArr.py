def FreqArr(arr):
    s={}
    for i in arr:
    	if(i not in s.keys()):
            s[i]=1
    	else:
            s[i]+=1
    print(s)
    for x,y in s.items():
    	print(type(x))
    	print(type(y))
    	print(x," ",y)
    
arr=[10,"k",10,15,10,12,12]
FreqArr(arr)
