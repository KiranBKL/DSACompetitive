import java.math.*;
public class BuildingProblem
{
	public static void main(String[] args) 
	{
		BuildingProblemProblem(2);
	}
	private static void BuildingProblemProblem(int n)
	{
		int zeros=1;
		int ones=1;
		for(int i=2;i<=n;i++)
		{
			int nzeros=ones;
			ones=zeros+ones;
			zeros=nzeros;
			//System.out.println(ones+zeros);
		}
		System.out.println((ones+zeros)*(ones+zeros));
	}
}