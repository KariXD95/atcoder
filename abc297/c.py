H,W = map(int,input().split())
for i in range(H):
    S = list(input())
    for j in range(0,W-1):
        if S[j] == "T" and S[j+1] == "T":
            S[j:j+1] = "P"
            S[j+1:j+2] = "C"
            
    print("".join(S))