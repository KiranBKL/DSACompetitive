def evalPostfix(s):
    s=s.split()
    #print(s)
    stack=[]
    l=['+','-','*','/','%']
    for i in reversed(s):
        if(i not in l):
            stack.append(i)
        else:
            a=stack.pop()
            b=stack.pop()
            #print(a+i+b)
           # print(type(eval(a+i+b)))
            res=eval(a+i+b)
            #print(res)
            stack.append(str(res))
    return stack[-1]
print(evalPostfix("+ * 2 3 9"))