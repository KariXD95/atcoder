S = input()
B1 = 0
B2 = 0
B1 = S.find("B") +1
for i in range(7,0,-1):
    if S[i] == "B":
        B2 = i+1
        break


R1 = S.find("R") +1
K = S.find("K") +1
R2 =0
for j in range(7,0,-1):
    if S[j] == "R":
        R2 = j+1
        break
        

if B1%2 == 0:
    if B2%2 ==0:
        print("No")
    if B2%2 ==1:
        if R1<K<R2:
            print("Yes")
        else:
            print("No")

if B1%2 ==1:
    if B2%2 ==1:
        print("No")
    else:
        if R1<K<R2:
            print("Yes")
        else:
            print("No")