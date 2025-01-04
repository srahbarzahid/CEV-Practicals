#include<stdio.h>
#include<stdlib.h>
#define MAX 50
int parent[MAX];
int rank[MAX];
void makeSet(int x) {
if (parent[x] != -1) {
printf("\nElement %d is already in the set\n", x);
return;
}
parent[x] = x;
rank[x] = 0;
printf("\nSet created for element %d\n", x);
}
int findSet(int x) {
if (parent[x] == -1) {
printf("\nElement %d is not in any set\n", x);
return -1;
}
if (parent[x] != x) {
parent[x] = findSet(parent[x]);
}
return parent[x];
}
void unionSets(int x, int y) {
int repX = findSet(x);
int repY = findSet(y);
if (repX == -1 || repY == -1) return;
if (repX != repY) {
if (rank[repX] > rank[repY]) {
parent[repY] = repX;
} else if (rank[repX] < rank[repY]) {
parent[repX] = repY;
} else {
parent[repY] = repX;
rank[repX]++;
}
printf("\nSets containing %d and %d have been merged\n", x, y);
} else {
printf("\nElements %d and %d are already in the same set\n", x, y);
}
}
void displaySets(int n) {
printf("\nElement : Parent\n");
for (int i = 1; i <= n; i++) {
if (parent[i] != -1) {
printf("%d : %d\n", i, findSet(i));
}
}

}
int main() {
int n = MAX;
for (int i = 0; i < n; i++) {
parent[i] = -1;
}
int choice, x, y;
do {
printf("1. Make Set\n");
printf("2. Find Set\n");
printf("3. Union Sets\n");
printf("4. Display Sets\n");
printf("5. Exit\n");
printf("Enter your choice: ");
scanf("%d", &choice);
switch (choice) {
case 1:
printf("\nEnter the element to create a set: ");
scanf("%d", &x);
makeSet(x);
break;
case 2:
printf("\nEnter the element to find its set: ");
scanf("%d", &x);
y = findSet(x);
if (y != -1) {
printf("The representative of %d is %d\n", x, y);
}
break;
case 3:
printf("\nEnter the first element: ");
scanf("%d", &x);
printf("Enter the second element: ");
scanf("%d", &y);
unionSets(x, y);
break;
case 4:
displaySets(n);
break;
case 5:
exit(0);
default:
printf("\nInvalid choice\n");
break;
}
} while (1);
return 0;
}
