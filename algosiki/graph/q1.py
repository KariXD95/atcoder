N,A,B = map(int,input().split())
S = []
for i in range(N):
    S.append(input())

def judge(A,B):
    if S[A][B] =="o":
        return True
    else:
        return False

if judge(A,B):
    print("Yes")
else:
    print("No")