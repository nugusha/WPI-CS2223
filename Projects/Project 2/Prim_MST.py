import heapq

dist = dict()  # distance
fix = dict()  # distance

def prim(graph,n):    # graph edges and number of vertieces
    for i in range(1,n+1): # initializing vertices
        dist[i] = 1000000000 #infinity
    
    adjList = [[] for _ in range(n+3)]
    
    for edge in graph:
        weight, x, y = edge
        adjList[x].append((weight,y))
        adjList[y].append((weight,x))
        
    h = []  # heap
    dist[1] = 0
    for i in range(1,n+1):
        fix[i] = 0
    heapq.heappush(h,(0,1,-1))   # push (a,b) - distance from 1 to b is a

    total_length = 0 # sum of edge weights in MST
    MST_Prim = set()
    

    total_length = 0

    
    while (len(MST_Prim)!=(n-1)):
        Distance, v1, v2 = heapq.heappop(h)

        if fix[v1] == 1: continue
        fix[v1] = 1
        total_length += Distance

        
        if v2!=-1:
            MST_Prim.add((Distance, min(v1,v2), max(v1,v2)))

        
        for x in adjList[v1]:
            weight, to = x
            if fix[to] == 0 and dist[to] > weight:
                dist[to] = weight
                heapq.heappush(h,(weight,to,v1))
            
        
    
#    return 4
    return MST_Prim
#    return total_length

N = 4
graph = set([           
            (1, 1, 2),   # (w,x,y) w-weight, x-vertex1, y-vertex2
            (5, 1, 3),
            (3, 1, 4),
            (4, 2, 3),
            (2, 2, 4),
            (1, 3, 4),
            ])
        
MST_Prim = set([
            (1, 1, 2),
            (2, 2, 4),
            (1, 3, 4),
            ])


# assert prim(graph,N) == MST_Prim
# assert prim(graph,N) == 4

