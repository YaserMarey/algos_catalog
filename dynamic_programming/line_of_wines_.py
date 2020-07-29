def maxProfit():
    P = [2, 4, 6, 2, 5]
    N = 5
    L = 0
    R = N - 1

    dp = [[0 for col in range(N)]
          for row in range(N)]

    # if (dp[L][R] != -1):
    #     return dp[L][R]

    year = N - (R - L)

    for i in range(0,5):
            dp[i][i] = i * P[i]

    dp[L][R] = max(P[L] * year + dp[L + 1][R], P[R] * year + dp[L][R - 1])

    return dp


# Driver code

# Price array
print(maxProfit());

