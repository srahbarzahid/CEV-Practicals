#include<stdio.h>
int main(){
 int n,a[20],temp;
 printf("enter length");
 scanf("%d",&n);
 printf("enter the data");
 
 for(int i=0;i<n;i++)
    scanf("%d",&a[i]);
 printf("before sorting\n");
 for(int i=0;i<n;i++)
   printf("%d ",a[i]);
    
  for(int i=0;i<n-1;i++){
    for(int j=0;j<n-i-1;j++){
       if(a[j]>a[j+1]){
       temp=a[j];
       a[j]=a[j+1];
       a[j+1]=temp;
       }
       }
     }
  printf("after sorting\n");
  for(int i=0;i<n;i++)
    printf("%d\n",a[i]); 
        
}
