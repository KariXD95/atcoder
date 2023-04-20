import sys
sys.setrecursionlimit(10**6)

N = int(input())
P = list(map(int,input().split()))
connect = [[] for i in range(N)]
for i in range(1,N):
    connect[P[i-1]].append(i)
ans = []

def DFS(now,pre):
    ans.append(now)
    for to in connect[now]:
        if to != pre:
            
            DFS(to,now)
            if now not in ans:
                ans.append(now)

DFS(0,-1)
print(*ans)
