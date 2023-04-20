N = int(input())
S = list(map(int,input().split()))
ans = []
for i in range(N):
    if(i == 0):
        ans.append(S[0])
    else:
        tmp =S[i] - S[i-1]
        ans.append(tmp)
print(*ans)