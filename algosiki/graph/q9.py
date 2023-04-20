import sys
sys.setrecursionlimit(10**6)

N = int(input())
P = list(map(int,input().split()))
connect = [[] for i in range(N)]

for i in range(1,N):
    connect[P[i-1]].append(i)

counter = [0]*N
count = 0
def DFS(now,pre,):
    
    for to in connect[now]:
        if to != pre:
            
            DFS(to,now)
            counter[now] +=count
            
 
    
            

DFS(0,-1)
print(counter)
