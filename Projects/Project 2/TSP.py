# time efficiency O(n!)
# space efficiency O(n^2)
fix = [0 ,0 ,0 ,0 ,0]  # distance
TSP_vertices = []
def TSP(vertex,dist,path=None):
    if path is None:
        path = [vertex]
    fix[vertex] = 1


    
    unused = 0
    for i in range(1,n+1):
        unused += 1 - fix[i]
 #   print(vertex,dist,path,unused)

    return_vertices = []

        
    if unused == 0:
        if weight[vertex][1]==-1:
            return 999999999,[]
        
        fix[vertex] = 0
        return dist+weight[vertex][1],path+[1]
    
    mi=999999999 # infinity

    for i in range(1,n+1):
        if i != vertex and fix[i]==0 and weight[vertex][i]!=-1:
            new_dist, new_list = TSP( i , dist + weight[vertex][i] , path + [i])
            if mi>new_dist:
                mi = new_dist
                return_vertices = new_list
    
    fix[vertex]= 0

    return mi,return_vertices

n = 4

weight = [[-1, -1, -1, -1, -1],
          [-1, -1, 1, 5, 3],
          [-1, 1, -1, 4, 2],
          [-1, 5, 4, -1, 10000000],
          [-1, 3, 2, 10000000, -1],]

print(TSP(1,0))
#assert TSP(1,0) == 6
