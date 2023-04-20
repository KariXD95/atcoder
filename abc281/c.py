N,T = map(int,input().split())
A = list(map(int,input().split()))
tmp = 0
cnt = 0

while (T >= tmp):
    for i in range(len(A)):
        tmp += A[i]
        cnt += 1
        if(T <= tmp):
            cnt1 = cnt%N
            tmp1 = A[i] - (tmp - T)
            print(cnt1,tmp1)
            exit()
        
print(cnt,tmp)


print(cnt1,tmp1)
#下　海斗の素晴らしいコード
N,T = map(int, input().split())
A = list(map(int, input().split()))

dd = T % sum(A)

I = 0
for i in range(N):
    if dd - A[i] > 0:
        dd = dd - A[i]
    else:
        I = i + 1 
        print(str(I) + ' ' + str(dd))
        exit()