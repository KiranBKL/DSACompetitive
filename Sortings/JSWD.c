#include <stdio.h>
int main(int argc, char const *argv[])
{
	int dead[5]={2,1,3,2,1};
	int pr[5]={12,2,22,32,21};
	int max=1;
	int i=0;
	int q[3];
	for(int k=1 ;k<=3;k++)
	{
		q[k]=-1;
	}
	for(i=0;i<5 && max<=3 ;i++)
	{
		for(j=0;j<5-i-1;j++)
		{
			if(pr[j]<pr[j+1])
			{
				m=pr[j];
				pr[j]=pr[j+1];
				pr[j+1]=m;
				n=dead[j];
				dead[j]=dead[j+1];
				dead[j+1]=n;
			}
		}
		
	}
	i=0;k=1;
	q[dead[i]]=i+1;
	k++;
	for(i=1;i<5 k<=3;i++)
	{
		int b=dead[i];
		while(q[b]!=-1)
		{
			b--;
		}
		q[b]=i+1;

	}
	
	return 0;
}