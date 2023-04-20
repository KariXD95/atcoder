N,M = map(int,input().split())
F = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    F[a].append(b)

for i in range(N):
    print(*sorted(F[i]))
