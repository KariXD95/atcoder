S = input()
count = 0
now = ""

for i in range(len(S)):
    now += S[i]
    count += 1
    
print(count - S.count("00"))
