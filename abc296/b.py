S = []
for i in range(8):
    s = input()
    S.append(s)
h = 0
w = 0
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            h = 8-i
            w = chr(97+j) 

print(w +str(h))