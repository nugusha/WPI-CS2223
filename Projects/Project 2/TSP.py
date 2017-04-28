# time efficiency O(n!)
# space efficiency O(n^2)
fix = [0 ,0 ,0 ,0 ,0]  # distance
TSP_vertices = set()
def TSP(vertex,dist,vertices):
    fix[vertex] = 1
    vertices.add(vertex)
    
    unused = 0
    for i in range(1,n+1):
        unused += 1 - fix[i]

        
    if unused == 0:
        return dist,vertices

    mi=999999999 # infinity

    for i in range(1,n+1):
        if i != vertex and fix[i]==0 and weight[vertex][i]!=-1:
            new_dist, new_set = TSP( i , dist + weight[vertex][i] , vertices)
            if mi>new_dist:
                mi = new_dist
                vertices = new_set

    fix[vertex]= 0


    return mi,vertices

n = 4

weight = [[-1, -1, -1, -1, -1],
          [-1, -1, 1, 5, 3],
          [-1, 1, -1, 4, 2],
          [-1, 5, 4, -1, 1],
          [-1, 3, 2, 1, -1],]
vertex_set = set()
print(TSP(1,0,vertex_set))
#assert TSP(1,0) == 6
