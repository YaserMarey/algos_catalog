# Given a set of positive numbers S, determine if there exists a subset whose sum is equal to a given number ‘C’.
# 0/1 Knapsack Pattern
# we are trying to find a subset of given numbers that has a total sum of C.
# so, C is the constraint that is it is similar to the capacity
# the difference is that we want the sum of the target set to be exactly equal to this amount C
# rather than to be as maximum as possible below the constraint that is the capacity such as in 0/1 Knapsack
# The sub-problem is the partial sum, partial set of numbers
# We want to try all combinations so we will loop from 1 to n the number of numbers in the set
# at each i will try to add all elements of the set provided it doesn't exceed the capacity which is the partial sum
# in our case here.
# the base case is when we don't have any capacity then the sum is equal to zero
# another base case which is when we have one element and then
# the sum will be equal to the one element value provided that it is less than the current target partial sum
# we will work out the solution from top to bottom one row at a time, and one column at a time from right to left
# the final sum will be the bottom right cell
# if the sum is equal to C then yes we found a subset, otherwise we didn't

# Reference implementation
def subset_sum(S, C):
    dp = [[0 for j in range(C + 1)] for i in range(len(S))]

    # with only one number, we can form a subset only when the required sum is
    # greater than its value
    for j in range(1, C + 1):
        if S[0] < C:  # C is the required sum
            dp[0][j] = S[0]

    # process all subsets for all sums
    for i in range(1, len(S)):
        for j in range(1, C + 1):

            if S[i] < j:
                dp[i][j] = max(dp[i - 1][j - S[i]] + S[i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # the bottom-right corner will have our answer.
    return (dp[len(S) - 1][C] == C)


def SS(S, C):
    T = [[0 for i in range(C + 1)] for j in range(len(S) + 1)]

    n = len(S)

    S = [0] + S

    # process all subsets for all sums
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            if S[i] <= j:
                T[i][j] = max(T[i - 1][j - S[i]] + S[i], T[i - 1][j])
            else:
                T[i][j] = T[i - 1][j]

    # the bottom-right corner will have our answer.
    return (T[n][C] == C)


def main():
    S = [1, 2, 3, 7]
    C = 6
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if SS(S, C) == subset_sum(S, C) else 'Fail', S, SS(S, C), subset_sum(S, C)))

    S = [1, 2, 7, 1, 5]
    C = 10
    print("Testcase 2 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if SS(S, C) == subset_sum(S, C) else 'Fail', S, SS(S, C), subset_sum(S, C)))

    S = [1, 3, 4, 8]
    C = 6
    print("Testcase 3 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if SS(S, C) == subset_sum(S, C) else 'Fail', S, SS(S, C), subset_sum(S, C)))


if __name__ == '__main__':
    main()
