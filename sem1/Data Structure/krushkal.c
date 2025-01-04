#include<stdio.h>
#include<stdlib.h>
# define MAX 100
int parent[MAX];

int find(int i){
	while(parent[i])
		i=parent[i];
	return i;	
	}
int uni(int i,int j){
	if(i!=j){
		parent[j]=i;
		return 1;
		}
	return 0;	
	}	

int main(){
	int v,cost_matrix[MAX][MAX];
	int edge_count,min_cost,i,edge1,edge2,count=1,sumcost=0,row_no,column_no;
	printf("enter the number of vertices: ");
	scanf("%d",&v);
		
		printf("enter the cost matrix:\n");
		for(int i=1;i<=v;i++){
			for(int j=1;j<=v;j++){
				scanf("%d",&cost_matrix[i][j]);
				if(cost_matrix[i][j]==0)
				   cost_matrix[i][j]=999;
				}
			}
			edge_count=v-1;
			
			while(count<=edge_count){
			for(i=1,min_cost=999;i<=v;i++){
			for(int j=1;j<=v;j++){
				if(cost_matrix[i][j]<min_cost){
						 min_cost=cost_matrix[i][j];
						 edge1=row_no=i;
						 edge2=column_no=j;
						 }
					}
				}
			row_no=find(row_no);
			column_no=find(column_no);
			
			if(uni(row_no,column_no)){
				printf("\nedge %d is %d->%d with cost:%d",count++,edge1,edge2,min_cost);
				sumcost+=min_cost;
				}
				cost_matrix[edge1][edge2]=cost_matrix[edge2][edge1]=999;
		}
		printf("\nsum cost: %d",sumcost);	
	}
