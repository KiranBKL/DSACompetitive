class MyStack
{
    int arr[];
    int cap,top;
    MyStack(int c)
    {
        cap=c;
        top=-1;
        arr=new int[cap];
    }
    void push(int k)
    {
        if((top+1)<cap)
        {
            top++;
            arr[top]=k;
        }
        else
        {
            System.out.println("Stack Overflow");
        }
    }
    int pop()
    {
        if(!isempty())
        {
            top--;
            return arr[top+1];
        }
        return top;
    }
    int size()
    {
        return top+1;
    }
    boolean isempty()
    {
        return (top==-1);
    }
    int peek()
    {   if(!isempty())
        return arr[top];
        else{return top}
    }
}