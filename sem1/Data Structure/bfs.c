#include<stdio.h>
#include<stdlib.h>
#define MAX 100
int graph[MAX][MAX], visited[MAX];
int v;

void bfs(int vertex){
	int queue[MAX],rear=0,front=0,current;
	visited[vertex]=1;
	queue[rear++]=vertex;
	
	printf("BFS Traversal: ");
	while(front<rear){
		current = queue[front++];
		printf("%d ",current);
		
		for(int i=0;i<v;i++){
			if(graph[current][i]==1 && !visited[i]){
				visited[i]=1;
				queue[rear++]=i;
				}
			}
		}
	}
	int main(){
		int start;
		printf("enter number of vertices");
		scanf("%d",&v);
		
		printf("adjancy matrix");
		for(int i=0;i<v;i++){
			for(int j=0;j<v;j++){
				scanf("%d",&graph[i][j]);
				}
			}
			for(int i=0;i<v;i++){
				visited[i]=0;
				}
				
				printf("starting vertex please: ");
				scanf("%d",&start);
				bfs(start);
		}
