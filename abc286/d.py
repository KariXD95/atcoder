N,X = map(int,input().split())
coin = []
for _ in range(N):
    a,b = map(int,input().split())
    coin.append([a,b])
print(coin)

dp = [[False]*(X+1) for i in range(N+1)]
print(dp)

for i in range(X+1):
    for j in range(N):
        if coin[j[0]] ==
            dp[i][j] = dp[i-1]dp[j]   