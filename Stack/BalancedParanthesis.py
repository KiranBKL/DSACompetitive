def check(a,b):
    return((a=='('and b==')') or (a=='[' and b==']') or (a=='{' and b=='}'))
def Balanced(str):
    stack=[]
    l=['(','[','{']
    l1=[')',']','}']
    for i in str:
        if(i in l):
            stack.append(i)
        else:
            if(not check(stack[-1],i)):
                return("No")
            else:
                stack.pop()
    return("Yes")
s=input("Enter the string")
print(Balanced(s))