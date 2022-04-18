#include <stdio.h>
void mergesort(int arr[],int l,int r);
void merge(int a[],int s,int mid,int e);
int main(int argc, char const *argv[])
{
	int a[20],s,e,m,n,i;
	printf("enter the length\n");
	scanf("%d",&n);
	printf("Enter the elements\n");
	for(int i=0;i<n;i++)
		scanf("%d",&a[i]);
	s=0,e=n-1;
	mergesort(a,s,e);
	for(i=0;i<n;i++)
	{
		printf("%d     ",a[i] );
	}
	return 0;
}
void mergesort(int arr[],int l,int r)
{
	if(l<r)
	{
		//for(int i=0;i<=r;i++)printf("%d",arr[i] );			
		int m=(l+r)/2;
		mergesort(arr,l,m);
		mergesort(arr,m+1,r);
		merge(arr,l,m,r);
	}
}
void merge(int a[],int s,int mid,int e)
{
	 int t[e-s+1],i=s,j=mid+1,k=0;
	while(i<=mid&&j<=e)
	{
		//printf("%d    %d\n",a[i],a[j] );
		if(a[i]<=a[j])
		{
			t[k]=a[i];
			i++;k++;
		}
		else{
			t[k]=a[j];
			j++;k++;
		}
	}
	//printf("\n");
	while(i<=mid)
	{
		t[k]=a[i];i++;k++;
	}
	while(j<=e)
	{
		t[k]=a[j];j++;k++;
	}
	for(int i=s;i<=e;i++)
	{
		a[i]=t[i-s];
		printf(" dd %d",a[i]);
	}
	printf("\n");
}