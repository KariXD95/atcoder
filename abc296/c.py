N,X = map(int, input().split())
A = set(map(int, input().split()))
for i in A:
    if i + X in A:
        print("Yes")
        exit()
print("No")