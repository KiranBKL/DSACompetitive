def maxsub(arr,k):
    q=[]
    for i in range(k):
        while q and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)
        l=[arr[j] for j in q ]
        print(l)
    for i in range(k,len(arr)):
        print(arr[q[0]])
        while len(q) and q[0]<=i-k:
            q.pop(0)
        while len(q) and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)
        #print(q)
        l=[arr[j] for j in q ]
        print(l)
    print(arr[q[0]])
    #print("\n")
    #print(q)
maxsub([10,8,5,12,15,7,8],3)