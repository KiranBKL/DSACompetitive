def Factorial(n):
    if(n==0):
        return 1
    return n*Factorial(n-1)
print(Factorial(5))