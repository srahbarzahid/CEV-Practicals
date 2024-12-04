#include<stdio.h>
#include<stdlib.h>

struct node{
   int data;
   struct node*left,*right;
  };
  struct node*root =NULL;
  struct node* create(int data)
  	{
  		struct node*newnode;
  		newnode=(struct node*)malloc(sizeof(struct node));
  		newnode->data=data;
  		newnode->left=newnode->right=NULL;
  		return newnode;
  	}
  struct node* insert(struct node*root, int data)
   	{
   		if(root==NULL)
   		    return create(data);
   		    
   		if(data < root->data) 
   			{
   				root->left=insert(root->left,data);
   			}
   		else
   		 	root->right=insert(root->right,data);	 
   		
   		
   		return root; 	  
   	}	
  
  struct node* inorder(struct node*root)
  	{
  	   if(root!=NULL)
  		{
  			inorder(root->left);
  			printf("%d ",root->data);
  			inorder(root->right);
  		}
  	}
  	
  	
  struct node* preorder(struct node* root)
   	{
   	   if(root!=NULL)
   		{
   			printf("%d ",root->data);
   			preorder(root->left);
   			preorder(root->right);
   		}
   	}	
  	
  	
  struct node* postorder(struct node*root)
       {
          if(root!=NULL)
             {
                postorder(root->left);
                postorder(root->right);
                printf("%d ",root->data);
             }
       	
       }
       
       
    int main()
      {
      	int opt,data;
      	
      	do{
      	   printf("\n1.insert\n");
      	   printf("2.inorder\n");
      	   printf("3.preorder\n");
      	   printf("4.postorder\n");
      	   printf("5.exit\n");
      	   printf("enter the option");
      	   scanf("%d",&opt);
      	   
      	   switch(opt)
      	   	{
      	   		case 1:printf("enter the data");
      	   			scanf("%d",&data);
      	   			root=insert(root,data);
      	   			printf("Value %d inserted into the BST.\n", data);
               		break;
               	case 2:printf("inorder traversal ");
               		inorder(root);	
               		break;
               	case 3: printf("preorder traversal ");
               		preorder(root);
               		break;
               	case 4:printf("postorder traversal ");
               		postorder(root);
               		break;
               	case 5:exit(0);
               	default:printf("invalid option..");			
      	   	}
      	}while(1);
      }   	
  	
  	
  	
  	
  	
  	
  		
