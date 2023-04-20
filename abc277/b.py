N = int(input())
str_1 = ["H","D","C","S"]
str_2 = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]

s = []
for i in range(N):
    tmp = str(input())
    a = tmp[0]
    b = tmp[1]
    if(a in str_1 and b in str_2 and not a+b in s):
        s.append(a+b)
    else:
        print("No")
        exit()
print("Yes")
        


