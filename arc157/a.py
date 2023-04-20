N,A,B,C,D = map(int,input().split())

if abs(B-C) >= 2:
    print("No")
elif B==0 and C==0 and A>0:
    if A>0 and D>0:
        print("No")
    else:
        print("Yes")
else:
    print("Yes")