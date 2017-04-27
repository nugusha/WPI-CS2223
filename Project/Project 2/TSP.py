# time efficiency O(n!)
# space efficiency O(n^2)
fix = [0 ,0 ,0 ,0 ,0]  # distance

def TSP(vertex,dist):
    fix[vertex] = 1
    
    unused = 0
    for i in range(1,n+1):
        unused += 1 - fix[i]

        
    if unused == 0:
        return dist

    mi=999999999 # infinity

    for i in range(1,n+1):
        if i != vertex and fix[i]==0 and weight[vertex][i]!=-1:
            mi = min ( mi , TSP( i , dist + weight[vertex][i]) )

    fix[vertex]= 0


    return mi

n = 4

weight = [[-1, -1, -1, -1, -1],
          [-1, -1, 1, 5, 3],
          [-1, 1, -1, 4, 2],
          [-1, 5, 4, -1, 1],
          [-1, 3, 2, 1, -1],]

print(TSP(1,0))
#assert TSP(1,0) == 6
