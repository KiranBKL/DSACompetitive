import numpy as np
def HousepaintCost(arr):
    column_length=len(arr[0])
    row_length=len(arr)
    #print(f"row length {row_length} and column length is {column_length}")
    dp=np.zeros(shape=(row_length,column_length),dtype=int)
    dp[0][0]=arr[0][0]
    dp[0][1]=arr[0][1]
    dp[0][2]=arr[0][2]
    #print(dp[1][0])
    #print("\n")
    for i in range(1,row_length):
        #print(i)
        dp[i][0]=arr[i][0]+min(dp[i-1][1],dp[i-1][2])
        dp[i][1]=arr[i][1]+min(dp[i-1][0],dp[i-1][2])
        dp[i][2]=arr[i][2]+min(dp[i-1][0],dp[i-1][1])
       # res=min(dp[row_length-1][0],min(dp[row_length-1][1],dp[row_length-1][2])
        
    print(dp)
    return min(dp[i])
arr=[
    [1,5,7],
    [5,8,4],
    [3,2,9],
    [1,2,4]
]
arr1=np.array(arr)
print(arr1.ndim)
#print(arr[1,1])
print(arr[1][1])
print(HousepaintCost(arr1))