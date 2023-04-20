# 218_b
P = list(map(int,input().split()))

# abc = "abcdefghijklmnopqrstuvwxyz"
# ans =""
# for i in range(26):
#     ans +=abc[P[i]-1]
# print(ans)


# chr(97) == "a"
ans =""
for i in range(26):
    ans +=chr(P[i]+96)
print(ans)