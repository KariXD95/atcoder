N,M  = map(int,input().split())
C = []
S = []
for i in range(M):
    tmp = int(input()) 
    C.append(tmp)
    S.append(set(map(int,input().split())))
print(C)
print(S)

ans = set()
for i in range(1,N+1):
    ans.add(i)

cnt = 0
for i in range(M):
    for j in range(i+1,M):
        tmp = S[i].union(S[j])
        if tmp == ans:
            cnt +=1

print(cnt)