N,K = map(int,input().split())
A = list(map(int,input().split()))

A_set = set(A)
tmp = sorted(A_set)[0:K]
tmp1 = set(tmp)
i = 0

while(True):
    if i not in tmp1:
        print(i)
        break
    else:
        i+=1