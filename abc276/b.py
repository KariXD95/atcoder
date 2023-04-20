N,M = map(int,input().split())
a = [list() for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    a[u-1].append(v)
    a[v-1].append(u)

for (i,v) in enumerate(a):
    v.sort()
    print(len(v), *v)