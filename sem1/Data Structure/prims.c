#include<stdio.h>
#include<stdlib.h>
# define MAX 100

int main(){
	int v,vertex[MAX],cost_matrix[MAX][MAX],visited[MAX]={0};
	int edge_count,min_cost,i,vertex1,vertex2,counter=1,sumcost=0;
	printf("enter the number of vertices: ");
	scanf("%d",&v);
	printf("enter the vertex: ");
	for(int i=1;i<=v;i++){
		scanf("%d",&vertex[i]);
		}
		
		printf("enter the cost matrix:\n");
		for(int i=1;i<=v;i++){
			for(int j=1;j<=v;j++){
				scanf("%d",&cost_matrix[i][j]);
				if(cost_matrix[i][j]==0)
				   cost_matrix[i][j]=999;
				}
			}
			visited[1]=1;
			edge_count=v-1;
			
			while(counter<=edge_count){
			for(i=1,min_cost=999;i<=v;i++){
			for(int j=1;j<=v;j++){
				if(cost_matrix[i][j]<min_cost){
					 if(visited[i]!=0){
						 min_cost=cost_matrix[i][j];
						 vertex1=i;
						 vertex2=j;
						 }
					}
				}
			}
			if(visited[vertex1]==0 || visited[vertex2]==0){
				printf("\nedge %d is %d->%d with cost:%d",counter++,vertex[vertex1],vertex[vertex2],min_cost);
				sumcost+=min_cost;
				visited[vertex2]=1;
				}
				cost_matrix[vertex1][vertex2]=cost_matrix[vertex2][vertex1]=999;
		}
		printf("\nsum cost: %d",sumcost);	
	}
