H,M = map(int,input().split())

def judge(h,m):
    ans = 0<=(h//10)*10+m//10<24 and 0<=(h%10)*10+m%10<=59
    return ans

while True:
    if(judge(H,M)):
        print(H,M)
        exit()
    else:
        M+=1
        if(M ==60):
            M =0
            H +=1
        if(H >=24):
            H = 0