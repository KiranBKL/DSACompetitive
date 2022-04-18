def DigitSum(n):
    if(n==0):
        return n
    return n%10+DigitSum(n//10)
print(DigitSum(500))