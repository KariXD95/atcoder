S = input()
table = [[0]*(len(S)+1)]*10

for i in range(len(S)):
    c = int(S[i])
    table[i+1] = table[i]
    table[i+1][c] = (table[i+1][c]+1)%2
print(table) 
