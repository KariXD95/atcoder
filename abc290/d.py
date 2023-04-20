T = int(input())

for i in range(T):
    N,D,K = map(int,input().split())
    x =0
    cnt =1
    marked = [0]    
    x = (x+D)%N

    while cnt <K:

        if x  not in marked:
            marked.append(x)
            cnt +=1
            x = (x+D)%N
        else:
            x = (x+1)%N
    print(marked[-1])