N = int(input())
W = list(map(str,input().split()))

for i in range(N):
    if W[i] == "and": 
        print("Yes") 
        exit()
    if W[i] == "not":
        print("Yes")
        exit()
    if W[i] == "that": 
        print("Yes") 
        exit()
    if W[i] == "the": 
        print("Yes") 
        exit()
    if W[i] == "you": 
        print("Yes")
        exit()
print("No")