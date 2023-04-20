import math
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

K = int(input())

k = factorization(K)


a = max(k)[0]*max(k)[1]

def judge(n):
    if(n % K == 0):
        return True
    else:
        return False

for i in range(a):
    if(judge(a)):
        print(a)
        exit()
    elif(judge(a-i)):
        print(a-i)
        exit()