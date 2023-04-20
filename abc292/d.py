import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

N,M = map(int,input().split())
G= np.array[[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
print(G)

