# abc201_b
N = int(input())
A = []
for i in range(N):
    S,T = map(str,input().split())
    T = int(T)
    A.append([T,S])
ans = sorted(A,reverse = True)[1][1]
print(ans)