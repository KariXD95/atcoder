# S = input()
# abc = "abcdefghijklmnopqrstuvwxyz"
# A = set()

# for i in range(len(S)):
#     if S[i] in abc:
#         if S[i] in A:
#             print("No")
#             exit()
#         else:
#             A.add(S[i])
    
#     if S[i] == ")":
#         A.clear()

# print("Yes")
# ↑は嘘解法　例[ "a()a" ]
# スタックを用いる

S = input()
abc = "abcdefghijklmnopqrstuvwxyz"
stack = []
box = []
for i in range(len(S)):
    if S[i] in abc:
        if S[i] in box:
            print("No")
            exit()
        else:
            stack.append(S[i])
            box.append(S[i])

    if S[i] == "(":
        stack.append("")
    
    if S[i] == ")":
        while True:
            tmp = stack.pop()
            if tmp == "":
                break
            else:
                box.remove(tmp)

print("Yes")
