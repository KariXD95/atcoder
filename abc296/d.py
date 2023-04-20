N, M = map(int, input().split())
lower = -1
upper = -1
if N*N < M:
    print(-1)
    exit()

for i in range(M,2,-1):
    if upper >0 and lower >0: break

    if M%i == 0:
        if N<i:
            continue
        if N>=i:
            lower = i
            while(True):
                if M%(i-1) == 0:
                    upper = i-1
                    break
                else:
                    i -=1
print(upper)            
