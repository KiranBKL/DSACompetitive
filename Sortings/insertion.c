#include<stdio.h>
int main(int argc, char const *argv[])
{
	int i,j,a[20],n,key;
	printf("dkgdajklfhadsjfkjasfjadkjfakjsfjdsk");
	printf("Enter the number\n");
	scanf("%d",&n);
	printf("Enter the numbers\n");
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
  }
    for(i=0;i<n;i++){
    printf("%d,",a[i]);
  }
	for(i=1;i<n;i++)
	{
		key=a[i];
		j=i-1;
		printf("\n%d\n",key);
		while(j>=0 && key<a[j])
		{
			printf("%d--a[j]",a[j]);
			a[j+1]=a[j];
			j=j-1;
		}
		a[j+1]=key;
	}
	for(i=0;i<n;i++){
		printf("%d,",a[i]);
  }
	return 0;
}