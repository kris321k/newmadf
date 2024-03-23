vertices=3


def print_matrix(distance2):
    for i in distance2:
        print(i)


def floywarshall(graph):
    distance2=[[0 for _ in range(vertices)] for _ in range(vertices)]
    for i in range(vertices):
        for j in range(vertices):
            distance2[i][j]=graph[i][j]


    
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if distance2[i][k]+distance2[k][j]<distance2[i][j]:
                    distance2[i][j]=distance2[i][k]+distance2[k][j]

        print_matrix(distance2)
        print("\n")






if __name__ =='__main__':
    graph=[[0 for _ in range(vertices)] for _ in range(vertices)]
    print("enter the vertices in the graph\n")
    for i in range(vertices):
        for j in range(vertices):
            k=int(input(f"enter the cost of the edge from{i} to {j}\n enter -1 for infinity: "))
            print("\n")
            if k==-1:
                graph[i][j]=float('inf')
            else:
                graph[i][j]=k

    floywarshall(graph)