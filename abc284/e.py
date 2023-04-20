import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
G = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False]*(N+1)
limit = 10**6
anser = 0

def DFS(now):
    global anser
    if anser == limit:
        print(anser)
        exit()

    for to in G[now]:
        anser +=1
        visited[now] = True
        if visited[to]:
            continue
        else:
            DFS(to)
    visited[now] = False
print(G)
DFS(1)
print(anser)