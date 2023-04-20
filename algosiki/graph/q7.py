import sys
sys.setrecursionlimit(10**6)

N = int(input())
P = list(map(int,input().split()))
connect = [[] for i in range(N)]

for i in range(1,N):
    connect[P[i-1]].append(i)
INF = float('inf')
v = [INF]*N
count = 0
def DFS(now,pre):
    global count
    v[now] = count
    for to in connect[now]:
        if to != pre:
            count += 1 
            DFS(to,now)
            count -= 1

DFS(0,-1)
for i in v:
    print(i)