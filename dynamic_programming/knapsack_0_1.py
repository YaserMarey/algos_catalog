# V is array of values for len(V) = len(W) items
# W is arrary of weights of len(V) = len(W) items
# B is bag capacity

def KS_0_1(V, W, C):
    T = [[0 for i in range(C + 1)] for j in range(len(V) + 1)]

    n = len(V)

    V = [0] + V
    W = [0] + W

    for i in range(1, n + 1):
        for j in range(1, C + 1):
            if W[i] <= j:
                T[i][j] = max(T[i - 1][j - W[i]] + V[i], T[i - 1][j])
            else:
                T[i][j] = T[i - 1][j]
    return T[n][C]


def main():
    W = [1, 2, 3, 5]
    V = [1, 6, 10, 16]
    B = 7
    print(
        'Test case 1: {0} maximum KS value is {1}'.format('Pass' if KS_0_1(V, W, B) == 22 else 'Fail', KS_0_1(V, W, B)))
    V = [1, 6, 10, 16]
    W = [1, 2, 3, 5]
    B = 5
    print(
        'Test case 1: {0} maximum KS value is {1}'.format('Pass' if KS_0_1(V, W, B) == 16 else 'Fail', KS_0_1(V, W, B)))
    V = [1, 6, 10, 16]
    W = [1, 2, 3, 5]
    B = 6
    print(
        'Test case 1: {0} maximum KS value is {1}'.format('Pass' if KS_0_1(V, W, B) == 17 else 'Fail', KS_0_1(V, W, B)))

if __name__ == '__main__':
    main()
