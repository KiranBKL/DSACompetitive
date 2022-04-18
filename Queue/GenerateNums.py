def gennum(n,l):
    q=[]
    for i in l:
        q.append(i)
    for i in range(0,n):
        cur=q.pop(0)
        print(cur)
        for j in l:
            q.append(cur+j)
l=['6','5']
l.sort()
print(l)
gennum(10,l)
