H,W = map(int,input().split())

ans = 0
for i in range(H):
    S = input()
    ans += S.count("#")
print(ans)