arr=["cab","code","bac","doce","abc"]
s=[]
s.append(arr[0])
while(s):
    for i in arr[1:]:
        print(set(s[0])," ",set(i))
        if(set(s[0])==set(i)):
            arr.remove(i)
        else:
            s.append(i)
    print(s.pop(0))
    
print(arr)
#for i in arr:
 #   if("".join(sorted(i)) not in s.keys()):
  #      print(i)
   #     s["".join(sorted(i))]=None
    