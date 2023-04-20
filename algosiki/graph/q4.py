N,M,X = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

friends = set(G[X])

res = set()
for i in G[X]:
    for j in G[i]:
        if j != X and not j in friends:
            res.add(j)

print(len(res))