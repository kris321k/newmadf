#include <stdio.h>
#include <limits.h>

void bellman_ford(int **graph, int vertices, int src)
{
    int distance[vertices];
    for (int t = 0; t < vertices; t++)
    {
        distance[t] = INT_MAX;
    }
    distance[src] = 0;

    for (int k = 0; k < vertices; k++)
    {
        for (int i = 0; i < vertices; i++)
        {
            for (int j = 0; j < vertices; j++)
            {

                if (distance[i] + graph[i][j] < distance[j])
                {
                    distance[j] = distance[i] + graph[i][j];
                }
            }
        }
    }
}

int main()
{
    printf("enter the graph\n");
    printf("enter the cost matrix\n");
    int vertices;
    scanf("%d", &vertices);
    int cost[vertices][vertices];
    int src, dest, weight;
    for (int i = 0; i < vertices; i++)
    {
        printf("enter the src dest and the weight");

        scanf("%d %d %d", &src, &dest, &weight);
        cost[src][dest] = weight;
    }

    return 0;
}