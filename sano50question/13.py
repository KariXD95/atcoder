# abc220_c
N = int(input())
A = list(map(int,input().split()))
X = int(input())

t = X//sum(A)
S = t*sum(A)
k = t*len(A)

for i in A:
    S += i
    k += 1
    if S>X:
        print(k)
        break