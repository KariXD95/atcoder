from collections import deque
n, q = map(int,input().split())
que = deque()
connect = [[] for _ in range(n+1)]
visited = [False]*(n+1)
counter = [0]*(n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)

for i in range(q):
    p,x = map(int,input().split())
    counter[p]+= x


que.append(1)
visited[1] = True

while(len(que)>0):
    now = que.popleft()
    now_number = counter[now]
    for to in connect[now]:
        if(visited[to] == False):
            counter[to]+=now_number
            visited[to]= True
            que.append(to)
print(*counter)