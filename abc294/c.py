N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

Anum = ""
Bnum = ""
Acount = 0
Bcount = 0

for i in range(N+M):
    if Acount <N and Bcount <M:
        if A[Acount] >B[Bcount]:
            Bnum +=str(i+1)+" "
            Bcount +=1
        else:
            Anum += str(i+1)+" "
            Acount +=1
    elif Acount >=N:
        Bnum += str(i+1)+" "
        Bcount +=1
    else:
        Anum +=str(i+1)+" "
        Acount +=1

print(Anum)
print(Bnum)
