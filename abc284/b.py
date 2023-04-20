T = int(input())
cnt = 0
for i in range(T):
    cnt = 0
    N = int(input())
    A = list(map(int,input().split()))
    
    for j in range(N):
        if A[j]%2 ==1:
            cnt+=1
    print(cnt)
