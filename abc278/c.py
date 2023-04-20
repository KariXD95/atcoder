N,Q = map(int,input().split())

s = set()

for i in range(Q):
    t,a,b = map(int,input().split())
    if(t==1):
        s.add((a,b))
    elif(t==2):
        s.discard((a,b))
    else:
        if((a,b) in s and (b,a) in s):
            print("Yes")
        else:
            print("No")