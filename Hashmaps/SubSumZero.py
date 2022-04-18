def SubSumZero(arr):
    s={}
    psum=0
    for i in arr:
        psum-=i
        print(psum)
        if(psum in s.keys()):
            return "it is There"
        if(psum==0):
            return "it is There"
        s[psum]=None
    return "Not there"
print(SubSumZero([1,2,3]))
print(SubSumZero([1,2,-3]))
print(SubSumZero([3,4,3,-1,1]))
print(SubSumZero([-3,4,-3,-1,1]))