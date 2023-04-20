N,Q = map(int,input().split())
status = [0]*N
for i in range(Q):
    c,x = map(int,input().split())
    if c ==1:
        status[x-1]+=1
    if c ==2:
        status[x-1]+=2
    if c ==3:
        if status[x-1] >= 2:
            print("Yes")
        else:
            print("No")