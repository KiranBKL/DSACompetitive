import numpy as np
def getMaxGold(arr):
	rl=len(arr)
	cl=len(arr[0])
	dp=np.zeros(shape=(rl,cl),dtype=int)
	for j in range(cl-1,-1,-1):
		for i in range(rl):
			if(j==cl-1):
				dp[i][j]=arr[i][j]
			elif(i==0):
				dp[i][j]=arr[i][j]+max(dp[i][j+1],dp[i+1][j+1])
			elif(i==rl-1):
				dp[i][j]=arr[i][j]+max(dp[i][j+1],dp[i-1][j+1])
			else:
				dp[i][j]=arr[i][j]+max(dp[i-1][j+1],max(dp[i][j+1],dp[i+1][j+1]))

	sol=dp[0][0]
	for i in range(rl):
		sol=max(sol,dp[i][0])
	print(sol)

gold = [[0,1,4,2,8,2],
    [4,3,6,5,0,4],
    [1,2,4,1,4,6],
    [2,0,7,3,2,2],
	[3,1,5,9,2,4],
	[2,7,0,8,5,1]]
arr=np.array(gold)
getMaxGold(arr)