def remov(s):
    stack=[]
    for i in s:
        if(len(stack)==0):
            stack.append(i)
        elif(stack[-1]!=i):
            stack.append(i)
        else:
            stack.pop()
    return stack
print(remov("aaa"))