def cal(petrol,dist):
    cp,pp,start=0,0,0
    for i in range(len(petrol)):
        cp+=(petrol[i]-dist[i])
        if(cp<0):
            start=i+1
            pp+=cp
            cp=0
    if (cp+pp)>=0:
        return start+1
    return -1
print(cal([50,10,60,100],[30,20,100,10]))