import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
G = [[] for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

ok = [False for i in range(N)]
cnt =0

def DFS(now,pre):
    global cnt
    for to in G[now]:
        if ok[to] == False:
            ok[to] = True
            DFS(to,now)
        if ok[to] == True:
            cnt +=1
            continue


ok[0] = True
DFS(0,-1)
print(M-N+cnt)


# if N-M >=2:
#     tmp = bool
#     DFS(0,-1)
#     for i in range(N):
#         if ok[i] == False:
#             tmp = False
#             break
#         else:
#             tmp = True
    
#     if tmp:
#         print(0)
#     else:
#         print()


# if N-M ==1:
#     tmp = bool
#     DFS(0,-1)
#     for i in range(N):
#         if ok[i] == False:
#             tmp = False
#             break
#         else:
#             tmp = True
    
#     if tmp:
#         print(1)
#     else:
#         print(0)

# if N-M ==0:
#     print(1)

# if N-M < 0:
#     print(2)
