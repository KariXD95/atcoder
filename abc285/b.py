N = int(input())
S = input()
l = 0
for i in range(N-1):
    l = 0
    for j in range(1,N//i):
        if S[j-1] != S[j+i-1]:
            l += 1
    print(l)
