N = int(input())
S = str(input())
count = 0
ans = ""
for i in S:
    if(i == '"'):
        count += 1
        ans += i
        
    elif(i == ',' and count%2 == 0):
        i = '.'
        ans += i
    else:
        ans += i
print(ans)