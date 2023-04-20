N = int(input())
X = list(map(int,input().split()))

X.sort()
for i in range(N):
    X.pop()
    X.pop(0)

ans = sum(X)/len(X)
print(ans)