from collections import deque, defaultdict
N = int(input())
connect = defaultdict(list)
que = deque()

for _ in range(N):
    a,b = map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)
que.append(1)
S = {1}
while len(que)>0:
    v = que.popleft()
    for i in connect[v]:
        if not i in S:
            que.append(i)
            S.add(i)
print(max(S)) 