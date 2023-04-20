from collections import defaultdict

N = int(input())
Q = int(input())

A = [[] for _ in range(N)]
B = defaultdict(set)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i = q[1]
        j = q[2]
        A[j-1].append(i)
        B[i-1].add(j)
    elif q[0] == 2:
        i = q[1]-1
        print(*sorted(A[i]))
    else:
        i = q[1]-1
        print(*sorted(list(B[i])))
