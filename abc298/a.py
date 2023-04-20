N = int(input())
S = input()

if "x" in S:
    print("No")
    exit()

if S.count("o") <1:
    print("No")
else:
    print("Yes")