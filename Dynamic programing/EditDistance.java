class EditDistance
{
       public static int minimum(int a, int b, int c) {
        return Integer.min(a, Integer.min(b, c));
    }
    private static int dist(String x, String y)
    {
        int m=x.length();
        int n=y.length();
        int cost;
        int[][] dp = new int[m+1][n+1];

        for(int i=1;i<=m;i++) 
        {
            dp[i][0]=i;               
        }
        for(int i=1;i<=n;i++)
        {
            dp[0][i]=i;
        }
        for(int i=1;i<=m;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(x.charAt(i-1)==y.charAt(j-1))
                {
                    cost=0;
                }
                else{
                    cost=1;
                }
                dp[i][j] = minimum(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+cost);
            }
        }
        return dp[m][n];
    }
 
    public static void main(String[] args)
    {
        String X = "kitten", Y = "sitting";
        System.out.print("The Levenshtein distance is " + dist(X, Y));
    }
}