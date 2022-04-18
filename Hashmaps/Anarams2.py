arr=["cab","code","bac","doce","abc"]
s={}
for i in arr:
    if("".join(sorted(i)) not in s.keys()):
        print(i)
        s["".join(sorted(i))]=None
    
