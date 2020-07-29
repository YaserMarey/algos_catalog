# Given an unlimited supply of coins, we would like to know if it is possible to
# form that sum to a target total
# Unbounded Knapsack Pattern

# O(nV) where n is the number of coins,
# V is the total value we want to change
def CCP_1(Coins, Total):
    dp = [[0 for _ in range(Total + 1)] for _ in range(len(Coins))]

    # process all subsets for all sub-totals
    for i in range(1, len(Coins)):
        for t in range(1, Total + 1):
            # include the coin, if it does not exceed the total
            if t >= Coins[i]:
                dp[i][t] = max(dp[i - 1][t], dp[i][t - Coins[i]] + Coins[i])
            else:
                dp[i][t] = dp[i - 1][t]
    # the bottom-right corner will the answer.
    # print(dp)
    return dp[len(Coins) - 1][Total] == Total


# antoher O(nV) where n is the number of coins,
# V is the total value we want to change

def CCP_2(Coins, Total):
    T = [False for _ in range(Total + 1)]
    T[0] = True
    for v in range(1, Total + 1):
        for i in range(0, len(Coins)):
            if Coins[i] <= v:
                if T[v - Coins[i]]:
                    T[v] = True
    return T[Total]


def main():
    Coins = [2, 5]
    Total = 7

    print("Testcase 1 CPP_1 is {0}, possibility to change {1} with set of coins {2} is: {3}"
          .format('Pass' if CCP_1(Coins, Total) else 'Fail', Total, Coins, CCP_1(Coins, Total)))

    print("Testcase 1 CPP_2 is {0}, possibility to change {1} with set of coins {2} is: {3}"
          .format('Pass' if CCP_2(Coins, Total) else 'Fail', Total, Coins, CCP_2(Coins, Total)))

    Coins = [2, 4]
    Total = 7

    print("Testcase 2 CPP_1 is {0}, possibility to change {1} with set of coins {2} is: {3}"
          .format('Pass' if not CCP_1(Coins, Total) else 'Fail', Total, Coins, CCP_1(Coins, Total)))

    print("Testcase 2 CPP_2 is {0}, possibility to change {1} with set of coins {2} is: {3}"
          .format('Pass' if not CCP_2(Coins, Total) else 'Fail', Total, Coins, CCP_2(Coins, Total)))


if __name__ == '__main__':
    main()
