import java.util.*;
class PreviousLargest
{
    public static void main(String args[])
    {
        Problem(new int[]{
            5,15,10,8,6,12,9,18
        });
    }
    private static void Problem(int[] arr)
    {
        int n=arr.length;
        int[] dp=new int[n];
        Stack<Integer> stack=new Stack<Integer>();
        stack.push(arr[0]);
        dp[0]=-1;
        for(int i=1;i<n;i++)
        {
            while(!(stack.empty()) && arr[i]>=stack.peek())
            {
                stack.pop();
            }
            if(stack.empty())
            {
                dp[i]=-1;
            }
            else{
                dp[i]=stack.peek();
            }
            stack.push(arr[i]);
        }
        for(int i=0;i<n;i++)
            System.out.print(dp[i]+" ");
    }
}