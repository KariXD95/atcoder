T = int(input())
for i in range(T):
    N = int(input())
    S = input()

    if S.count("1") == 2:
        double_one = S.count("11")
        if double_one == 1:
            num_double = S.find("11")
            if S[0:num_double].count("00") >= 1 or S[num_double+2:N].count("00") >=1:
                print(2)
            else:
                if S[0:num_double].count("0") >=1 and S[num_double+2:N].count("0") >=1:
                    print(3)
                else:
                    print(-1)
        else:
            print(1)

    else:
        if S.count("1")%2 == 1:
            print(-1)
        else:
            print(S.count("1")//2)
    