N = int(input())
S = []
for i in range(N):
    tmp = input()
    S.append(tmp)
S.reverse()
for i in range(N):
    print(S[i])