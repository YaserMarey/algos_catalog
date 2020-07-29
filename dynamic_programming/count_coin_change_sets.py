# Given an unlimited supply of coins, we would like to know how many sets of coins
# we can form that sum to a target total
# Unbounded Knapsack Pattern

# Reference implementation
def count_of_coins_change_sets(Coins, Total):
    dp = [[0 for _ in range(Total + 1)] for _ in range(len(Coins))]

    # sum = 0 means empty set, and empty set is always achievable for any set, therefore count = 1
    for i in range(0, len(Coins)):
        dp[i][0] = 1

    # process all subsets for all sub-totals
    for i in range(0, len(Coins)):
        for t in range(1, Total + 1):
            # exclude the number, or carry out the count from previous set
            dp[i][t] = dp[i - 1][t]
            # include the coin, if it does not exceed the totla
            if t >= Coins[i]:
                dp[i][t] += dp[i][t - Coins[i]]
    # the bottom-right corner will the answer.
    return dp[len(Coins) - 1][Total]


# This implementation doesn't pass all the test cases
def CCS(C, Total):
    # Ini
    T = [[0 for j in range(Total + 1)] for i in range(len(C) + 1)]

    # Base case
    # sum = 0 means empty set, and empty set is always achievable for any set, therefore count = 1
    # It is noticalbe that when there is a count of something, usually the base case is 1
    for i in range(0, len(C)): T[i][0] = 1

    n = len(C)
    C = [0] + C

    # process all subsets for all sub-totals
    for i in range(1, n + 1):
        for t in range(1, Total + 1):
            # Carry out the count from previous set
            T[i][t] = T[i - 1][t]
            # Include the coin, if it does not exceed the totla
            if C[i] <= t:
                T[i][t] = T[i][t] + T[i][t - C[i]]
    # the bottom-right corner will the answer.
    return T[n][Total]


# Antoher valid implementation, easier to understand, the only trick applied here
# is the fact that we add 1 to previous count if we can add the coin to the set

def CCS_(C, Total):
    # Ini
    T = [[0 for j in range(Total + 1)] for i in range(len(C) + 1)]

    # Base case
    # sum = 0 means empty set, and we assume that we can not achieve empty set
    for i in range(0, len(C)): T[i][0] = 0

    n = len(C)
    C = [0] + C

    # process all subsets for all sub-totals
    for i in range(1, n + 1):
        for t in range(1, Total + 1):
            # Include the coin, if it does not exceed the total
            if C[i] <= t:
                T[i][t] = max(T[i - 1][t], T[i][t - C[i]] + 1)
    # the bottom-right corner will the answer.
    return T[n][Total]


def main():
    Coins = [1, 2, 3]
    Total = 5
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CCS_(Coins, Total) == count_of_coins_change_sets(Coins, Total)
                  else 'Fail', Coins, CCS_(Coins, Total), count_of_coins_change_sets(Coins, Total)))

    Coins = [1, 2, 3]
    Total = 3
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CCS_(Coins, Total) == count_of_coins_change_sets(Coins, Total)
                  else 'Fail', Coins, CCS_(Coins, Total), count_of_coins_change_sets(Coins, Total)))


if __name__ == '__main__':
    main()
