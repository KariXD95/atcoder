# N, K, D を受け取る
N, K, D = map(int, input().split())

# A を受け取る
A = list(map(int, input().split()))

# S を計算する
S = set()
for i in range(N):
    for j in range(i+1, N+1):
        S.add(sum(A[i:j]))

# S 中の D の倍数の最大値を求める
result = -1
for x in S:
    if x % D == 0:
        result = max(result, x)

# 結果を出力する
print(result)
