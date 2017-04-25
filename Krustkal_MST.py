parent = dict() # parent vertex
depth = dict()  # maximum depth down from the vertex

def find(x):        # disjoint set union - finding root
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):   # unifying two vertices a and b
    A = find(a)
    B = find(b)
    if A != B:
        if depth[A] > depth[B]:
            parent[B] = A
        else:
            parent[A] = B
            if depth[A] == depth[B]: depth[B] += 1 # updating depth

def kruskal(graph,n):    # graph edges and number of vertieces
    for i in range(1,n+1): # initializing vertices
        parent[i] = i
        depth[i] = 1

    MST_Krustkal = set()
    
    edges = list(graph)
    edges.sort()        # sorting edges by length
    
    for edge in edges:
        len, start, end  = edge
        if find(start) != find(end): # checking if vertices are in 
            MST_Krustkal.add(edge)   # different trees
      #      print(edge)
            union(start, end)
        
    return MST_Krustkal

N = 4
graph = set([
            (1, 1, 2),
            (5, 1, 3),
            (3, 1, 4),
            (4, 2, 3),
            (2, 2, 4),
            (1, 3, 4),
            ])
        
MST_Krustkal = set([
            (1, 1, 2),
            (2, 2, 4),
            (1, 3, 4),
            ])


assert kruskal(graph,N) == MST_Krustkal

