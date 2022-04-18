import java.math.*;
public class KnapSack
{
	public static void main(String[] args) 
	{
		KnapSackProblem(new int[] {2,5,1,3,4}, new int[] {15,14,10,45,30},7);
	}
	private static void KnapSackProblem(int[] wts,int[] vals,int cap)
	{
		int[][] dp=new int[wts.length][cap+1];
		for(int i=0;i<dp.length;i++)
		{
			if(i==0)
            {
                for(int j=wts[i];j<dp[0].length;j++)
                {
                    dp[i][j]=vals[i];
                }
            }
            for(int j=1;j<dp[0].length;j++)
            {
                if(j<)
            }
		}
		System.out.println(dp[wts.length][cap]);
	}
	
}