N,K = map(int,input().split())
A = list(map(int,input().split()))
S = []
for i in range(N):
    S.append(list(map(int,input().split())))
print(S)
print(A)
print(S[A[0]-1])
