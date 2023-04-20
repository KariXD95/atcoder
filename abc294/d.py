N,Q = map(int, input().split())

num = 0
Set2 = set()

for i in range(Q):
    E = list(map(int, input().split()))
    if E[0] == 1:
        Set2.add(num)
        num += 1
    elif E[0] == 2:
        Set2.remove(E[1]-1)
    elif E[0] == 3:
        print(list(Set2)[0]+1)