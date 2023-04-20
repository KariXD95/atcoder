import sys
sys.setrecursionlimit(10**6)

H,W = map(int,input().split())
A = []
for i in range(H):
    a = list(map(int,input().split()))
    A.append(a)
print(A)
ans = 0
visited = []
ok = [[False]*W]*H
print(ok)
def DFS(h,w):
    for i in range(H+W-2):

        if w != W-1 and ok[h][w+1] == False:
            w += 1
            print(w)
            ok[h][w] = True
            visited.append(A[h][w])
            if h == H-1 and w == W-1:
                tmp = set()
                tmp = set(visited)
                if len(tmp) == H+W-1:
                    ans +=1
            DFS(h,w)
            visited.pop()
            w -=1
            ok[h][w] = False
        
        if h != H-1 and ok[h+1][w] == False:
            h += 1
            ok[h][w] = True
            visited.append(A[h][w])
            if h == H-1 and w == W-1:
                tmp = set()
                tmp = set(visited)
                if len(tmp) == H+W-1:
                    ans +=1
            DFS(h,w)
            visited.pop()
            h -=1
            ok[h][w] = False

visited.append(A[0][0])
ok[0][0] = True
DFS(0,0)
print(visited)
print(ok)
print(ans)