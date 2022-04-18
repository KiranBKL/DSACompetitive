/import java.math.*;
public class GroupArrangment
{
	public static void main(String[] args) 
	{
		GroupArrangmentProblem(5,3);
	}
	private static void GroupArrangmentProblem(int n,int k)
	{
		int[][] dp=new int[k+1][n+1];
		for(int i=0;i<dp.length;i++)
		{
			for(int j=0; j<dp[0].length;j++)
			{
				if(i==0 || j==0 || j<i)
				{
					dp[i][j]=0;
				}
				else if(i==1 || i==j )
				{
					dp[i][j]=1;
				}
				else{
					dp[i][j]=i*dp[i][j-1]+dp[i-1][j-1];
				}

				System.out.println(dp[i][j]);
			}
			System.out.println("\n");
		}
		System.out.println(dp[k][n]);
	}
}