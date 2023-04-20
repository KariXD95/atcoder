N,K = map(int,input().split())
S = input()
stack = ""
ans = ""
for i in range(N):
    if len(stack) == K:
        ans += "x"*(N-i)
        break

    if S[i] == "o":
        stack +="o"
        ans +="o"
    else:
        ans+="x"
print(ans)