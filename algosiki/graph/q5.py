N,X = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,-1)
res = 0
while X != 0:
    res +=1
    X = A[X]
print(res)