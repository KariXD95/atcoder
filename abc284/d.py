T = int(input())

while T>0 : 
    N = int(input())

    for i in range(2,N):
        if N%i ==0:
            if N%(i**2) ==0:
                p = i
                q = N//(i**2)
                print(p,q)
                break
            else:
                q = i
                p = int((N//i)**(0.5))
                print(p,q)
                break  
    T -=1