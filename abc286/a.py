N,P,Q,R,S = map(int, input().split())
A = list(map(int, input().split()))

a1 = A[0:P-1]
a2 = A[P-1:Q]
a3 = A[Q:R-1]
a4 = A[R-1:S]
a5 = A[S:N]

res = a1 + a4 + a3 + a2 + a5
res_str = ''

for i in res:
    res_str += str(i) + ' '

print(res_str[0:len(res_str)-1])