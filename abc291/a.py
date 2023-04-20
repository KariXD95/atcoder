S = input()
ans = 0
for i in range(len(S)):
    if S[i].isupper():
        ans = i
        break

print(ans+1)