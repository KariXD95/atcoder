S = input()
T = input()
ans = 0

for i in range(len(S)):
    if(T[i] != S[i]):
        ans = i+1
        break
    else:
    #if(S[len(S)-1] == T[len(S)-1]):
        ans = len(S)+1
print(ans)