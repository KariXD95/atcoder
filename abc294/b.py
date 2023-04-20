H,W = map(int,input().split())
matrix = []
ans = ""
for i in range(H):
    A = list(map(int,input().split()))
    matrix.append(A)
for i in range(H):
    if i>=1:
        print(ans)
        ans =""
    for j in range(W):
        if matrix[i][j] ==0:
            ans+="."
        else:
            ans+=chr(64+matrix[i][j])
print(ans)