N,D = map(int,input().split())
T = list(map(int,input().split()))
T.append(float('inf'))
for i in range(N):
    if T[i+1]-T[i] <= D:
        print(T[i+1])
        exit()
print(-1)