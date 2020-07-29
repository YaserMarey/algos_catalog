# Given a set of positive numbers S, determine if there exists a subset whose sum is equal to a given number ‘C’.
# 0/1 Knapsack Pattern

# Reference implementation
def count_subset_sum(S, C):
        dp = [[0 for x in range(C + 1)] for y in range(len(S))]

        # sum = 0 means empty set, and empty set is always achievable for any set, therefore count = 1
        for i in range(0, len(S)):
            dp[i][0] = 1

        # when sum of one element set equal to the  with only one number,
        # we can form a subset only when the required sum is equal to its value
        for s in range(1, C + 1):
            dp[0][s] = 1 if S[0] == s else 0

        # process all subsets for all sums
        for i in range(1, len(S)):
            for s in range(1, C + 1):
                # exclude the number
                dp[i][s] = dp[i - 1][s]
                # include the number, if it does not exceed the sum
                if s >= S[i]:
                    dp[i][s] += dp[i - 1][s - S[i]]
        # the bottom-right corner will the answer.
        # print (dp)
        return dp[len(S) - 1][C]


def CSS(S, C):
    T = [[0 for j in range(C + 1)] for i in range(len(S) + 1)]

    # Ini
    n = len(S)

    S = [0] + S
    # sum = 0 means empty set, and empty set is always achievable for any set, therefore count = 1
    for i in range(0, n):
        T[i][0] = 1

    # process all subsets for all sums
    for i in range(1, n + 1):
        for s in range(1, C + 1):
            # exclude the number
            T[i][s] = T[i - 1][s]
            # include the number, if it does not exceed the sum
            if s >= S[i]:
                T[i][s] = T[i][s] + T[i - 1][s - S[i]]
    # the bottom-right corner will the answer.
    return T[n][C]

def main():
    S = [1, 1, 2, 3]
    C = 4
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CSS(S, C) == count_subset_sum(S, C) else 'Fail', S, CSS(S, C), count_subset_sum(S, C)))

    S = [1, 2, 7, 1, 5]
    C = 9
    print("Testcase 2 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CSS(S, C) == count_subset_sum(S, C) else 'Fail', S, CSS(S, C), count_subset_sum(S, C)))

    S = [1, 2, 3]
    C = 7
    print("Testcase 3 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CSS(S, C) == count_subset_sum(S, C) else 'Fail', S, CSS(S, C), count_subset_sum(S, C)))

if __name__ == '__main__':
    main()
