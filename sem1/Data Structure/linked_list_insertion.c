#include<stdio.h>
#include<stdlib.h>

struct node
  {
	int data;
	struct node*next;	
  };
  
  struct node*newnode,*temp,*head=NULL;
  
  void begin()
   {
   	newnode = (struct node*)malloc(sizeof(struct node));
   	printf("enter the data: ");
   	scanf("%d",&newnode->data);
   	
  	if(head==NULL)
  	   {
  		head=newnode;
  		head->next = NULL; 
  	   }
  	else
           {
  	 	newnode->next = head;
  	 	head = newnode;	
  	   }	
   }
   
   void end()
   {
   	struct node*temp;
   	newnode = (struct node*)malloc(sizeof(struct node));
   	printf("enter the data to be insert: ");
   	scanf("%d",&newnode->data);
   	
   	if(head==NULL)
   	   {
   	   	head=newnode;
   	   	head->next=NULL;
   	   }
    	else
    	   {
    	   	temp=head;
    	   	while(temp->next!=NULL)
    	   	   {
    	   	   	temp=temp->next;
    	   	   }
    	   	temp->next=newnode;
    	   	newnode->next = NULL; 
    	   }   
   }
   
   
   void middle()
   {
   	struct node*temp;
   	int pos,i=1;
   	newnode = (struct node*)malloc(sizeof(struct node));
   	printf("enter the position: ");
   	scanf("%d",&pos);
   	
   	if(head==NULL)
   	   {
   	   	printf("the list is empty");
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
   	        
   	        printf("enter the data: ");
   		scanf("%d",&newnode->data);
   		
   	   	newnode->next=temp->next;  
   	   	temp->next=newnode;
   	   }   
   }
   
   void search()
   {
   	struct node*temp;
   	int flag = 0,data,count=1;
   	 
   	printf("enter the data to be search: ");
   	scanf("%d",&data);
   	
   	if(head==NULL)
   	    {
   	    	printf("list is empty.\n");
   	    	return;
   	    }
   	else
   	  {
   	  	temp=head;
   	  	while(temp->next!=0)
   	  	    {
   	  	    	if(data==temp->data)
   	  	    	    {
   	  	    	    flag=1;
   	  	    	    break;
   	  	    	    }
		        temp=temp->next;
		        count++;	   	  	    	    
   	  	    }
   	 	if(flag==1)
   	 	   {
   	 	   	printf("the data %d is found at position %d\n",data,count);
   	 	   } 
   	 	else
   	 	  {
   	 	  	printf("the data %d not found",data);
   	 	  }      
   	  }    
   	 
   }
   
   void display()
   {
   	struct node*temp;
   	temp=head;
   	if(head==NULL)
   	  {
   	  	printf("list is empty");
   	  }
   	else
   	  {
   	  	while(temp!=0)
   	  		{
   	  			printf(" %d ",temp->data);
   	  			temp=temp->next;
   	  		}
   	  }
   }
   
   
   int main()
   {
   	int opt;
   	do
   	 {
   	 	printf("\n1.insert at beginning\n");
   	 	printf("2.insert at end\n");
   	 	printf("3.insert at specified position\n");
   	 	printf("4.display\n"); 
   	 	printf("5.search the data\n");
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
   
   
   
   
   
   
   
   
   
