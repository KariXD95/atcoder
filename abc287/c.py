import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

ok = [False for i in range(N)]

def DFS(now,pre):
    for to in G[now]:
        if ok[to] == False:
            ok[to] = True
            DFS(to,now)

if M != (N-1):
    print("No")
    exit()

for i in range(N):
    if len(G[i]) >2:
        print("No")
        exit()       
            
ok[0] =True
DFS(0,-1)
tmp = bool
for i in ok:
    if i == False:
        tmp = False
        break

if tmp:
    print("Yes")
else:
    print("No")