#Line of wine recursively
def S(L, R, Y, P):
    if (L==R):
        return Y*P[L]
    return max(S(L+1,R, Y+1, P) + Y*P[L], S(L,R-1, Y+1, P) + Y*P[R])

def S_():
    S = [[0] * 5 for i in range(5)]
    P = [2, 4, 6, 2, 5]
    Y = 1
    L = 0
    R = 4
    for i in range(0,int(5/2)):
            S[i][i] = (i+1)*2*P[(i+1)*2]
    print(S)

    for L in range(0,5):
        for R in range(4, -1, -1):
            if (L+1) + (R+1) > 5:
                continue
            S[L][R] = max(S[L+1][R] + Y * P[L], S[L][R - 1] + Y * P[R])
            Y += 1
    print(S)
    print (max(max(S)))




def main():
    P = [2, 4, 6, 2, 5]
    Y = 1
    L = 0
    R = 4
    print(S(L, R, Y, P))
    S_()

if __name__ == '__main__':
    main()
