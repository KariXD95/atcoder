N = int(input())
S = input()

now = [0,0]
visited =[(0,0)]

for i in range(N):
    if S[i] == "R":
        now[0]+=1
        visited.append(tuple(now))
    if S[i] == "L":
        now[0]-=1
        visited.append(tuple(now))
    if S[i] == "U":
        now[1]+=1
        visited.append(tuple(now))
    if S[i] == "D":
        now[1]-=1
        visited.append(tuple(now))

cnt1 = len(visited)
tmp = set(visited)
cnt2 = len(tmp)

if cnt1 == cnt2: print("No")
else: print("Yes")
