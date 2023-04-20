n,q = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

for i in range(q):
    x = int(input())
    if(a[0]>=x):
        print(n)
    elif(a[n-1]<x):
        print(0)
    else:
        l = 0
        r = n-1
        while(r-l>1):
            mid = (r+l)//2
            if(a[mid]<x):
                l = mid
            else:
                r = mid
        print(n-r)