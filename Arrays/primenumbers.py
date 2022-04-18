n=int(input())
for i in range(2,n+1):
    for j in range(2,n):
        if i%j==0:
            break
    if(j==n):
        print(j,end=" ")