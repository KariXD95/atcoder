N = int(input())
agree = 0
disagree = 0
for i in range(N):
    tmp = input()

    if tmp == "For":
        agree += 1
    else:
        disagree +=1

if agree > disagree:
    print("Yes")
else:
    print("No")