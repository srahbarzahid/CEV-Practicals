#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 10

// Vertex structure
struct vertex {
    char data;
    bool visited;
};

// Graph data structures
struct vertex* graph[MAX];   // Array of vertices
int adj_matrix[MAX][MAX];    // Adjacency matrix
int vertex_count = 0;        // Count of vertices

// Queue for BFS
int queue[MAX], front = 0, rear = -1;

// Enqueue and Dequeue functions
void enqueue(int data) {
    queue[++rear] = data;
}

int dequeue() {
    return queue[front++];
}

bool is_queue_empty() {
    return front > rear;
}

// Add a vertex
void add_vertex(char data) {
    struct vertex* new_vertex = (struct vertex*)malloc(sizeof(struct vertex));
    new_vertex->data = data;
    new_vertex->visited = false;
    graph[vertex_count++] = new_vertex;
}

// Add an edge
void add_edge(int start, int end) {
    adj_matrix[start][end] = 1;
    adj_matrix[end][start] = 1;  // For undirected graph
}

// Display vertex
void display_vertex(int vertex_index) {
    printf("%c ", graph[vertex_index]->data);
}

// Get an unvisited adjacent vertex
int get_unvisited_adjacent_vertex(int vertex_index) {
    for (int i = 0; i < vertex_count; i++) {
        if (adj_matrix[vertex_index][i] == 1 && !graph[i]->visited) {
            return i;
        }
    }
    return -1;
}

// BFS traversal
void bfs(int start_vertex) {
    printf("BFS Traversal: ");

    // Mark the start vertex as visited and enqueue it
    graph[start_vertex]->visited = true;
    display_vertex(start_vertex);
    enqueue(start_vertex);

    while (!is_queue_empty()) {
        int current_vertex = dequeue();
        int adj_vertex;

        // Visit all unvisited adjacent vertices
        while ((adj_vertex = get_unvisited_adjacent_vertex(current_vertex)) != -1) {
            graph[adj_vertex]->visited = true;
            display_vertex(adj_vertex);
            enqueue(adj_vertex);
        }
    }
    printf("\n");

    // Reset all vertices to unvisited
    for (int i = 0; i < vertex_count; i++) {
        graph[i]->visited = false;
    }
}

int main() {
    int option, start, end, start_vertex;
    char vertex_data;

    // Initialize adjacency matrix
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            adj_matrix[i][j] = 0;
        }
    }

    do {
        printf("\n1) Add Vertex\n2) Add Edge\n3) Perform BFS\n0) Exit\nChoose an option: ");
        scanf("%d", &option);

        switch (option) {
            case 1:
                printf("Enter vertex data: ");
                scanf(" %c", &vertex_data);
                add_vertex(vertex_data);
                break;

            case 2:
                printf("Enter edge start and end (indices): ");
                scanf("%d %d", &start, &end);
                if (start >= vertex_count || end >= vertex_count) {
                    printf("Invalid edge! Vertices do not exist.\n");
                } else {
                    add_edge(start, end);
                }
                break;

            case 3:
                printf("Enter starting vertex index: ");
                scanf("%d", &start_vertex);
                if (start_vertex >= vertex_count) {
                    printf("Invalid starting vertex!\n");
                } else {
                    bfs(start_vertex);
                }
                break;

            case 0:
                printf("Exiting...\n");
                break;

            default:
                printf("Invalid option. Try again.\n");
        }
    } while (option != 0);

    return 0;
}
