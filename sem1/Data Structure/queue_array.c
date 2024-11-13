#include<stdio.h>
#include<stdlib.h>
#define N 10

int queue[N];
int rear=-1,front=-1;

void enqueue()
   {
   int val;
   printf("enter the data");
   scanf("%d",&val);
   
   if(rear==N-1)
   	{
   	  printf("queue is overflow\n");
   	  return;
   	}
   else if(rear==-1 && front==-1) 
   	{
   		rear=front=0;
   		queue[rear]=val;
   	} 
   else
     {
   	rear++;
   	queue[rear]=val;
     }	  	
   }
   
void dequeue()
   {
   	if(rear==-1 && front==-1)
   	 {
   		printf("queue is underflow\n");
   		return;
   	 }
   	else if(rear==front)
   	  {
   	  printf("deleted element is %d",queue[front]);
   	   rear=front=-1;
   	  } 
   	else
   	  {
   	  	printf("deleted element is %d",queue[front]);
   	  	front++;
   	  	
   	  } 
   } 
   
 void display()
   {
        int i;
   	if(rear==-1 && front==-1)
   	   {
   	   	printf("queue is underflow\n");
   	   	return;
   	   }
   	else   
          {
          	for(i=front;i<=rear;i++)
          	   printf("%d ",queue[i]); 
          }		
   }    
   
   
 int main()
   {
   	int opt;
   	do
   	  {
   	  	printf("\n1.enqueue\n");
   	  	printf("2.dequeue\n");
   	  	printf("3.display\n");
   	  	printf("4.exit\n");
   	  	printf("enter the option ");
   	  	scanf("%d",&opt);
   	  	
   	  	switch(opt)
   	  	   {
   	  	   	case 1:enqueue();
   	  	   		break;
   	  	   	case 2:dequeue();
   	  	   		break;
   	  	   	case 3:display();
   	  	   		break;
   	  	   	case 4:exit(0);
   	  	   	default:printf("invalid option");			
   	  	   }
   	  }while(1);
   }  
   
   
   
   
   
