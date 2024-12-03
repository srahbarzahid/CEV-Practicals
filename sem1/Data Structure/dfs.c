#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 6  // Maximum number of vertices

// Vertex structure
struct vertex {
    char data;
    bool visited;
};

// Global variables
struct vertex* graph[MAX];
int adj_matrix[MAX][MAX] = {0};  // Adjacency matrix initialized to 0
int stack[MAX], top = -1;       // Stack for DFS
int vertex_count = 0;           // Number of vertices

// Add a vertex
void add_vertex(char data) {
    struct vertex* new_vertex = (struct vertex*)malloc(sizeof(struct vertex));
    new_vertex->data = data;
    new_vertex->visited = false;
    graph[vertex_count++] = new_vertex;
}

// Add an edge to the adjacency matrix
void add_edge(int start, int end) {
    adj_matrix[start][end] = 1;
    adj_matrix[end][start] = 1;  // For undirected graph
}

// Push a vertex onto the stack
void push(int data) {
    stack[++top] = data;
}

// Pop a vertex from the stack
int pop() {
    return stack[top--];
}

// Check if the stack is empty
bool is_stack_empty() {
    return top == -1;
}

// Find an unvisited adjacent vertex
int get_unvisited_adjacent(int vertex) {
    for (int i = 0; i < vertex_count; i++) {
        if (adj_matrix[vertex][i] == 1 && !graph[i]->visited) {
            return i;
        }
    }
    return -1;
}

// Display a vertex
void display_vertex(int vertex) {
    printf("%c ", graph[vertex]->data);
}

// Perform Depth-First Search
void dfs() {
    printf("DFS Traversal: ");
    graph[0]->visited = true;  // Start with the first vertex
    display_vertex(0);
    push(0);

    while (!is_stack_empty()) {
        int unvisited = get_unvisited_adjacent(stack[top]);
        if (unvisited == -1) {
            pop();
        } else {
            graph[unvisited]->visited = true;
            display_vertex(unvisited);
            push(unvisited);
        }
    }

    // Reset visited status for all vertices
    for (int i = 0; i < vertex_count; i++) {
        graph[i]->visited = false;
    }
    printf("\n");
}

int main() {
    int option, start, end;
    char data;

    do {
        printf("\n1) Add Vertex\n2) Add Edge\n3) DFS Traversal\n0) Exit\nChoose an option: ");
        scanf("%d", &option);

        switch (option) {
            case 1:
                if (vertex_count < MAX) {
                    printf("Enter vertex data: ");
                    scanf(" %c", &data);
                    add_vertex(data);
                } else {
                    printf("Maximum vertices reached!\n");
                }
                break;

            case 2:
                printf("Enter start vertex index: ");
                scanf("%d", &start);
                printf("Enter end vertex index: ");
                scanf("%d", &end);
                if (start >= 0 && start < vertex_count && end >= 0 && end < vertex_count) {
                    add_edge(start, end);
                } else {
                    printf("Invalid vertex index!\n");
                }
                break;

            case 3:
                dfs();
                break;

            case 0:
                printf("Exiting...\n");
                break;

            default:
                printf("Invalid option, try again.\n");
        }
    } while (option != 0);

    return 0;
}
