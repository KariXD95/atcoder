n = int(input())

a = []
b = []

for i in range(n):
    a.append(list(map(int,input().split())))
    
for i in range(n):
    b.append(list(map(int,input().split())))

    
def rotate():
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n - i - 1] = a[i][j]
            
    return tmp
            
def check():
    for i in range(n):
        for j in range(n):
            if a[i][j] and not b[i][j]:
                return False
            
    return True

for _ in range(4):
    a = rotate()
    if check():
        print("Yes")
        exit()

print("No")