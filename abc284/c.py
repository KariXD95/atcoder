class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1: return x 
        else:
          self.par[x] = self.root(self.par[x]) 
          return self.par[x]

    
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False 
        
        if self.rank[rx] < self.rank[ry]: 
            rx, ry = ry, rx
        self.par[ry] = rx 
        if self.rank[rx] == self.rank[ry]: 
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] 
        return True
    
   
    def size(self, x):
        return siz[root(x)]


N, M = map(int, input().split())


uf = UnionFind(N)


for i in range(M):
   
    a, b = map(int, input().split())

    
    uf.unite(a-1, b-1)


result = 0
for v in range(N):
    if uf.root(v) == v:
        result += 1
print(result)