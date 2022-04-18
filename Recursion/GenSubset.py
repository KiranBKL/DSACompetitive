def subset(s,curr,i):
    if(i==len(s)):
        print(curr)
        return
    subset(s,curr,i+1)
    subset(s,curr+s[i],i+1)
subset("ABC","",0)