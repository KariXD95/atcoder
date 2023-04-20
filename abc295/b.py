R,C = map(int,input().split())
B = []
for i in range(R):
    b = list(input())
    B.append(b)


for j in range(R):
    for k in range(C):
        if B[j][k].isdigit():
            for r in range(R):
                for c in range(C):
                    if int(B[j][k]) >= abs(k-c)+abs(j-r) and B[r][c] == "#":
                        B[r][c] = "."

for j in range(R):
    for k in range(C):
        if B[j][k].isdigit():
            B[j][k] = "."

for j in range(R):
    ans = ""
    for k in range(C):
        ans += B[j][k]
    print(ans)
        