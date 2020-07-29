# Given an infinite supply of 'n' coin denominations and a total money amount,
# we are asked to find the minimum number of coins needed to make up that amount.
# Unbounded Knapsack Pattern

import math


def minimum_count_of_coins(Coins, Total):
    dp = [[math.inf for _ in range(Total + 1)] for _ in range(len(Coins))]

    # for sum = 0 we need 0 coins
    for i in range(0, len(Coins)):
        dp[i][0] = 0

    # process all subsets for all sub-totals
    for i in range(1, len(Coins)):
        for t in range(1, Total + 1):
            # include the coin, if it does not exceed the totla
            if t >= Coins[i]:
                dp[i][t] = min(dp[i][t - Coins[i]] + 1, dp[i - 1][t])
            else:
                # exclude the number, or carry out the count from previous set
                dp[i][t] = dp[i - 1][t]

    # the bottom-right corner will the answer.
    return dp[len(Coins) - 1][Total]


def MCS(Coins, Total):
    dp = [[math.inf for j in range(Total + 1)] for i in range(len(Coins))]

    # for sum = 0 we need 0 coins
    for i in range(0, len(Coins)):
        dp[i][0] = 0

    # process all subsets for all sub-totals
    for i in range(1, len(Coins)):
        for t in range(1, Total + 1):
            # include the coin, if it does not exceed the totla
            if t >= Coins[i]:
                dp[i][t] = min(dp[i][t - Coins[i]] + 1, dp[i - 1][t])
            else:
                # exclude the number, or carry out the count from previous set
                dp[i][t] = dp[i - 1][t]

    # the bottom-right corner will the answer.
    return dp[len(Coins) - 1][Total]

def main():
    C = [1, 2, 3]
    Total = 5
    A = [0, 5, 6]
    print(
        "Testcase 1 is {0} for coins denominations {1}, and Total {2} since it is calculated as {3} and it should be {3}"
        .format('Pass' if MCS(C, Total) == minimum_count_of_coins(C, Total) else 'Fail', C, Total,
                MCS(C, Total), minimum_count_of_coins(C, Total)))

    C = [1, 2, 3]
    Total = 11
    print(
        "Testcase 1 is {0} for coins denominations {1}, and Total {2} since it is calculated as {3} and it should be {3}"
        .format('Pass' if MCS(C, Total) == minimum_count_of_coins(C, Total) else 'Fail', C, Total,
                MCS(C, Total), minimum_count_of_coins(C, Total)))

    C = [1, 2, 3]
    Total = 7
    print(
        "Testcase 1 is {0} for coins denominations {1}, and Total {2} since it is calculated as {3} and it should be {3}"
        .format('Pass' if MCS(C, Total) == minimum_count_of_coins(C, Total) else 'Fail', C, Total,
                MCS(C, Total), minimum_count_of_coins(C, Total)))

    C = [3, 5]
    Total = 7
    print(
        "Testcase 1 is {0} for coins denominations {1}, and Total {2} since it is calculated as {3} and it should be {3}"
        .format('Pass' if MCS(C, Total) == minimum_count_of_coins(C, Total) else 'Fail', C, Total,
                MCS(C, Total), minimum_count_of_coins(C, Total)))


if __name__ == '__main__':
    main()
