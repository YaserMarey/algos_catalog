# Given a ribbon of length 'n' and a set of possible ribbon cuts.
# We need to cut the ribbon into the maximum number of pieces.
# We would like to know the the count of pieces.

import math
def MRC(Cuts, Total):
    dp = [[-math.inf for _ in range(Total + 1)] for _ in range(len(Cuts))]

    for i in range(len(Cuts)):
        dp[i][0] = 0

    for i in range(0, len(Cuts)):
        for t in range(1, Total + 1):
            if i > 0:
                dp[i][t] = dp[i - 1][t]
            if t >= Cuts[i]:
                dp[i][t] = max(dp[i][t], dp[i][t - Cuts[i]] + 1)

    return dp[len(Cuts) - 1][Total]


def main():
    print(MRC([2, 3, 5], 5))  # should return 2
    print(MRC([2, 3], 7))  # should return 3
    print(MRC([3, 5, 7], 13))  # should return 3
    print(MRC([3, 5], 7))  # should return -inf


main()
