import math
def mostBalloons(N, arr):
        # Code here 
        if (N<=2): 
            return N        
        maxBalloons = 2
        for i in range(N): 
            slope={} 
            vertical,horizontal,identical=0,0,0              
            for j in range(i+1,N):  
                    if (arr[i]==arr[j]): 
                        identical+=1 
                    elif (arr[i][0]==arr[j][0]): 
                        vertical+=1  
                    elif (arr[i][1]==arr[j][1]): 
	                    horizontal+=1
                    else: 
	                    ydiff= arr[i][1]-arr[j][1]
	                    xdiff= arr[i][0]-arr[j][0]
	                    
	                    gcd = math.gcd (abs(ydiff),abs(xdiff)) 
	                    ydiff//=gcd 
	                    xdiff//=gcd
	                    if (xdiff<0): 
	                        xdiff*=-1 
	                        ydiff*=-1
	                    if (ydiff, xdiff) in slope: 
	                        slope[(ydiff, xdiff)]+=1 
	                    else: 
	                        slope[(ydiff, xdiff)]=1
            print(slope)
            if len(slope):
                maxBalloons=max(maxBalloons,1+identical+max(slope.values()))
            maxBalloons=max(maxBalloons,1+identical+max(vertical,horizontal)) 
        return maxBalloons
print(mostBalloons(4,[[1,2],[2,3],[2,1],[3,4]]))