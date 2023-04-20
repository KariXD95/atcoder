N,X,Y = map(int,input().split())
A = []
A.append(X)
A.append(Y)
for i in range(2,N):
    num = (A[i-2]+A[i-1])%100
    A.append(num)

print(A[N-1])