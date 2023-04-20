N = int(input())
S = input()
if S[0] == "M": Male = True
if S[0] == "F": Male = False
for i in range(N):
    if S[i] == "M" and Male:
        Male = False
        continue
    if S[i] == "F" and not Male:
        Male = True
        continue
    else:
        print("No")
        exit()
print("Yes")