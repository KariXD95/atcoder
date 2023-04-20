K = int(input())
l = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ans = []
for i in range(K):
    ans.append(l[i])

print(*ans,sep = "")