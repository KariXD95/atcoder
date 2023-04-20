from collections import defaultdict
N,M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

student ,max_num = -1, -1
for i in range(N):
    num = len(G[i])
    if max_num < num:
        max_num = num
        student = i

G[student].sort()
print(*G[student])