import java.util.Scanner;
class StackTest
{
    public static void main(String args[])
    {
        MyStack s=new MyStack(5);
        Scanner scan=new Scanner(System.in);
        while(true)
        {
            System.out.println("1.Enter 1 for pushing,2 for poping,3 forsize,4 for isempy and 5 for peek");
            int n=scan.nextInt();
            if(n==1)
            {
                int n1=scan.nextInt();
                s.push(n1);
            }
            else if(n==2)
            {   int k=s.pop();
                if(k!=-1)
                {
                    System.out.println(k);
                }
                else{
                    System.out.println("Stack Under Flow"); 
                }
            }
            else if(n==3)
            {
                System.out.println(s.size());
            }
            else if(n==4)
            {
                System.out.println(s.isempty());
            }
            else if(n==5)
            {
                System.out.println(s.peek());
            }
            else{
                break;
            }
        }
    }
}