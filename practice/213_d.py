import sys
sys.setrecursionlimit(10**6)
N = int(input())
connect = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)

for i in range(N+1):
    connect[i].sort()
print(connect)
ans = []

def DFS(now,pre):
    ans.append(now)
    for to in connect[now]:
        if to !=pre:
            DFS(to,now)
            ans.append(now)

DFS(1,-1)
print(ans)