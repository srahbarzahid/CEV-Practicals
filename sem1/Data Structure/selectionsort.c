#include<stdio.h>
void main()
{
	int n,a[100],min;
	printf("enter length");
	scanf("%d",&n);
	printf("enter data");
	for(int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
  	}
 
	for(int i=0;i<n-1;i++)
	{
		min=i;
  		for(int j=i+1;j<n;j++)
  		{
        		if(a[j]<a[min])
        		{
        			min=j;
        		}
       			}
       	       int temp=a[i];
		       a[i]= a[min];
		       a[min]=a[i];		
	}		
  
 	 printf("after sorting\n");
 	 for(int i=0;i<n;i++)
 	 {
	 	printf("%d\n",a[i]);
	 }   
  
  
}
