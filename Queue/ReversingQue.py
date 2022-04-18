def rev(l):
    if(len(l)==0):
        return
    x=l[-1]
   # print(l)
    l.pop(0)
    print(l)
    rev(l)
    print(x)
    l.append(x)
print(rev(['1','2','3','4']))