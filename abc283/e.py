H,W = map(int,input().split())
A = []
count = 0
ok = True
for i in range(H):
    tmp = list(map(int,input().split()))
    A.append(tmp)
print(A)

for i in range(H):
    for j in range(W):
        if A[i][j] == A[i][j+1] or A[i][j] == A[i+1][j] or A[i][j] == A[i-1][j] or A[i][j] == A[i][j-1]:
            ok = True
        else:
            for k in range(W):
                