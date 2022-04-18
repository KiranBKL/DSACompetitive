def I2P(exp):
    #exp=exp.split()
    priority={'+':1,'-':1,'*':2,'/':2,'%':3,'**':4,'(':0,')':0}
    #print('-' in priority)
    res=''
    stack=[]
    for i in reversed(exp):
        if(i not in priority):
            res+=i
        elif(i=='('):
            stack.append(i)
        elif(i==')'):
            while stack and stack[-1]!='(':
                res+=stack.pop()
            if stack:
                stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[i]<=priority[stack[-1]]:
                res+=stack.pop()
            stack.append(i)
       # print(res," ",stack)
    while stack:
        res+=stack.pop()
    return res[::-1]
#print(I2P("(A+(C+D*F+T*A)*B/C))"))
print(I2P("A+B"))