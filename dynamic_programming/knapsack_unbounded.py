# Reference implementation
def KS_unbounded(V, W, B):
    dp = [[0 for _ in range(B + 1)] for _ in range(len(W))]
    # if we have only one weight, we will take it if it is not more than the B
    for c in range(0, B + 1):
        if W[0] <= c:
            dp[0][c] = V[0]

    for i in range(0, len(V)):
        for c in range(1, B + 1):
            if W[i] <= c:
                dp[i][c] = max(dp[i][c - W[i]] + V[i], dp[i - 1][c])
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[len(W) - 1][B]


def KSU(V, W, B):
    # Ini and base case
    dp = [[0 for j in range(B + 1)] for i in range(len(V) + 1)]

    n = len(V)

    V = [0] + V
    W = [0] + W

    for i in range(1, n + 1):
        for c in range(1, B + 1):
            if W[i] <= c:
                dp[i][c] = max(dp[i][c - W[i]] + V[i], dp[i - 1][c])
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][B]

def main():
    W = [1, 2, 3]
    V = [15, 20, 50]
    B = 5
    print('Test case 1: {0} maximum KS value is {1}'.format('Pass' if KSU(V, W, B) == KS_unbounded(V, W, B) else 'Fail',
                                                            KS_unbounded(V, W, B)))
    V = [15, 50, 60, 90]
    W = [1, 3, 4, 5]
    B = 8
    print('Test case 1: {0} maximum KS value is {1}'.format('Pass' if KSU(V, W, B) == KS_unbounded(V, W, B) else 'Fail',
                                                            KS_unbounded(V, W, B)))
    V = [15, 50, 60, 90]
    W = [1, 3, 4, 5]
    B = 6
    print('Test case 1: {0} maximum KS value is {1}'.format('Pass' if KSU(V, W, B) == KS_unbounded(V, W, B) else 'Fail',
                                                            KS_unbounded(V, W, B)))

if __name__ == '__main__':
    main()
