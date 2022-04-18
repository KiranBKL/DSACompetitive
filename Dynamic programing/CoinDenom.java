import java.math.*;
public class CoinDenom
{
	public static void main(String[] args) 
	{
		CoinSum(new int[]
		{
			2,3,5
		},7);
	}
	private static void CoinSum(int[] arr,int tar)
	{
		int[] dp=new int[tar+1];
		dp[0]=1;
		for(int i=0;i<arr.length;i++)
		{
			for(int j=arr[i];j<dp.length;j++)
			{
				dp[j]+=dp[j-arr[i]];
			}
		}
		System.out.println(dp[tar]);
	}
	private static void targetSumSubset(int[] arr, int target)
	{
		int n=arr.length;
		boolean[][] dp=new boolean[n+1][target+1];
		for(int i=0;i<dp.length;i++)
		{
			for(int j=0;j<dp[0].length;j++)
			{
				if(i==0)
				{
					dp[i][j]=false;
				}
				else if(j==0)
				{
					dp[i][j]=true;
				}
				else 
				{
					if(dp[i-1][j]==true)
					{
						dp[i][j]=true;
					}
					else
					{
						int val=arr[i-1];
						if(j>=val)
						{
							if(dp[i-1][j-val]==true)
							{
								dp[i][j]=true;
							}
						}
					}
				}
			}
		}
		System.out.println(dp[arr.length][target]);
	}
	private static void goldMineProblem(int[][] arr)
	{
		int rl=arr.length;
		int cl=arr[0].length;
		int[][] dp = new int[rl][cl];
		for(int j = cl-1; j >= 0; j--)
		{
			for (int i = rl-1; i>=0; i--) 
			{
				if(j == cl-1)
				{
					dp[i][j]=arr[i][j];
				}
				else if(i==0)
				{
					dp[i][j]=arr[i][j]+Math.max(dp[i][j+1],dp[i+1][j+1]);
				}
				else if(i==rl-1)
				{
					dp[i][j]=arr[i][j]+Math.max(dp[i][j+1],dp[i-1][j+1]);
				}
				else
				{
					dp[i][j]=arr[i][j]+Math.max(dp[i][j+1],Math.max(dp[i-1][j+1],dp[i+1][j+1]));
				}
			}
		}
		int max=dp[0][0];
		for(int i=0;i<rl;i++)
		{
			if(dp[i][0]>max)
			{
				max=dp[i][0];
			}
		}
		System.out.println(max);
	}
}