#include<stdio.h>
#include<stdlib.h>

struct node
  {
	struct node*pre;
	int data;
	struct node*next;
  };
  struct node*head=NULL,*temp,*newnode;
  
  void begin()
    {
    	newnode = (struct node*)malloc(sizeof(struct node));
    	printf("enter the data");
    	scanf("%d",&newnode->data);
    	newnode->next=0;
    	newnode->pre=0;
    	
    	if(head==NULL)
    	  {
    	  	head=newnode;
    	  	head->pre=0;
    	  	head->next=0;
    	  }
    	else
    	  {
    	    	head->pre=newnode;
		newnode->next=head;
		head=newnode;    	    
    	  }  
    }
    
    
  void end()
     { 
     	struct node*temp;    
     	newnode = (struct node*)malloc(sizeof(struct node));
     	printf("enter the data");
     	scanf("%d",&newnode->data);
     	
     	if(head==NULL)
     	 {
     	 	head=newnode;
     	 	head->next=0;
     	 	head->pre=0;
     	 }
     	else
     	  {
     	  	temp=head;
     	  	while(temp->next!=0)
     	  	 {
     	  	  temp=temp->next;
     	  	 }
     	  	temp->next=newnode;
     	  	newnode->pre=temp;
     	  	newnode->next=0; 
     	  } 
     }
     
  void middle()
     {
     	int pos,data,i=1;
     	struct node*temp;
     	newnode = (struct node*)malloc(sizeof(struct node));
     	printf("enter the position");
     	scanf("%d",&pos);
     	
     	if(head==NULL){
     		printf("invalid postion");
     		return;
     		}
	else
	  {
	  	temp=head;
	  	while(i<pos-1)
	  	  {
	  	  	temp=temp->next;
	  	  	i++;
	  	  }
	  	printf("enter the data");
     	        scanf("%d",&newnode->data);
     	        
	  	newnode->pre=temp;
	  	newnode->next=temp->next;
	  	temp->next=newnode;
	  	newnode->next->pre=newnode;  
	  }   	     			
     }
     
       void search()
     {
     	int data,flag=0,count=1;
     	struct node*temp;
     	printf("enter the data to be search");
     	scanf("%d",&data);
     	
     	if(head == NULL)
     		{
     			printf("the list is empty");
     			return;
     		}
     	else
     	  {
     		temp=head;
     		while(temp!=0)
     		    {
     		    	if(data==temp->data)
     		    	    {
     		    	    flag=1;
     		    	    break;
     		    	    }
     		    	temp=temp->next;
     		    	count++;
     		    
     		    }
     	  }
     	  if(flag==1){
     	      printf("the value is found at %d",count);}
         else{  
              printf("the value cannot be find");
     	     }
     	  	
     		
     }
         
   void display()
   {
   	struct node*temp;
   	temp=head;
   	if(head==NULL){
   	 	printf("list is empty");
   	 	return;}
   	 else
   	 {
   	 	while(temp!=0)
   	  	{
   	  		printf("%d ",temp->data);
   	  		temp=temp->next;
   	  	}
   	 }	
   }
   
   
   int main()
   {
   int opt;
   do{
   	
     printf("\n1.insert at beginning\n");
   	 	printf("2.insert at end\n");
   	 	printf("3.insert at specified position\n");
   	 	printf("4.display\n"); 
   	 	printf("5.search\n");
   	 	printf("6.exit\n");
   	 	printf("choose an option ");
   	 	scanf("%d",&opt);
   	 	
   	 	switch(opt)
   	 	   {
   	 	     case 1: begin();
   	 	             break;
		     case 2: end();
		             break;
		     case 3: middle(); 
		             break;
		     case 4: display();
		             break;	
		     case 5: search();
		     	      break;  	        		             
		     case 6: exit(0);        
		     default: printf("invalid option\n");                 		       	   	 	            
   	 	   }
   	 }while(opt!=0);
   }  
     
     
       
