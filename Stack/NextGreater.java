import java.util.*;
class NextGreater
{
    public static void main(String args[])
    {
        NextGreater(new int[]{
            5,15,10,8,6,12,9,18
        });
    }
    private static void NextGreater(int[] arr)
    {
        Stack<Integer> stack=new Stack<Integer>();
        int n=arr.length;
        int[] dp=new int[n];
        stack.push(arr[n-1]);
        dp[n-1]=-1;
        for(int i=n-2;i>=0;i--)
        {
            while(!(stack.empty()) && arr[i]>=stack.peek())
            {
                stack.pop();
            }
            if(stack.empty())
            {
                dp[i]=-1;
            }
            else
                dp[i]=stack.peek();
            stack.push(arr[i]);
        }
        for(int i=0;i<n;i++)
            System.out.print(dp[i]+" ");
    }
}