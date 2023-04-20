S = input()

def judge(S):
    if(len(S) != 8):
        return False
    if(not S[1:7].isdecimal()):
        return False
    elif(S[0].isupper()):
        if(not float(S[1:7]).is_integer()):
            return False
        if( 100000<=int(S[1:7])<=999999 ):
            if(S[7].isupper()):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

if(judge(S)):
    print("Yes")
else:
    print("No")
