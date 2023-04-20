N,K = map(int,input().split())
S = []
for i in range(N):
    tmp = input()
    S.append(tmp)

X = []
for i in range(K):
    X.append(S[i])

X.sort()

for i in range(K):
    print(X[i])
