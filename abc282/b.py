N, M = map(int,input().split())
S = [input() for i in range(N)]
res = 0
print(S)
for i in range(N):
    for j in range(i+1,N):
        ok = True
        for k in range(M):
            if(S[i][j] == "x" and S[j][k] == "x"):
                ok = False
        if(ok):
            res += 1
print(res)