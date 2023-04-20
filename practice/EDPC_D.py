N,W = map(int, input().split())

dp = [[0]*(W+1) for i in range(N+1)]
# i  =1~N
for i in range(1,N+1):
    wi,vi = map(int,input().split())
    # w= 0~N
    for w in range(0,W+1):
        
        if(w - wi<0):
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w],dp[i-1][w-wi]+vi)

print(dp[N][W])