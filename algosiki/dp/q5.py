N,M = map(int,input().split())
A = list(map(int,input().split()))
INF = 1000000
dp = [INF]*(N)
dp[0] = 0

for i in range(1,N):
    for j in range(1, M+1):
        if i-j >=0:
            dp[i] = min(dp[i], dp[i-j]+A[i]*j)
print(dp[N-1])