N = input()
A = list(map(int, input().split()))

dict = {}
for i in A:
    if not i in dict.keys():
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1

ans = 0

for i in dict.values():
    ans += int(i/2)

print(ans)