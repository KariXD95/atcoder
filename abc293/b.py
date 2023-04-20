N = int(input())
A = list(map(int,input().split()))
call = [0]*N
compare = set(range(1,N+1))
tmp = set()

for i in range(N):
    if call[i] == 0:
        call[A[i]-1] +=1
        tmp.add(A[i])
    else:
        continue

compare -=tmp
K = len(compare)
ans = list(compare)
ans.sort()
print(K)
print(*ans)