N,M = map(int,input().split())
a = list(map(int,input().split()))

ans = []
tmp = []

for i in range(1,N+1):
    tmp.append(i)
    if i not in a:
        ans += tmp[::-1]
        tmp = []

print(*ans)

        