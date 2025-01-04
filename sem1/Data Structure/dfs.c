#include<stdio.h>
#include<stdlib.h>
#define MAX 100

int graph[MAX][MAX];
int visited[MAX];
int v;

void dfs(int vertex){
	visited[vertex]=1;
	printf("%d ",vertex);
	for(int i=0;i<v;i++){
		if(graph[vertex][i]==1 && !visited[i]){
		dfs(i);
		}
		}
	}
	int main(){
		printf("enter the number of vertices");
		scanf("%d",&v);
		printf("enter matrix");
		for(int i=0;i<v;i++){
			for(int j=0;j<v;j++){
				scanf("%d",&graph[i][j]);
				}
			}
			for(int i=0;i<v;i++){
				visited[i]=0;
				}
				printf("starting vertex is 0 \n");
				dfs(0);
		}
