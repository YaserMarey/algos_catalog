# Given a set of positive numbers, find if we can partition it into two subsets such that the
# sum of elements in both the subsets is equal.
# 0/1 Knapsack Pattern
# we are trying to find a subset of given numbers that has a total sum of 's/2'.
# so, sum(S)/2 is the constraint that is it is similar to the capacity
# the difference is that we want the sum of the target set to be exactly equal to this amount sum(S)/2
# rather than to be as maximum as possible below the constraint that is the capacity such as in 0/1 Knapsack
# The sub-problem is the partial sum, partial set of numbers
# We want to try all combinations so we will loop from 1 to n the number of numbers in the set
# at each i will try to add all elements of the set provided it doesn't exceed the capacity which is the partial sum
# in our case here.
# the base case is when we don't have any capacity then the sum is equal to zero
# another base case which is when we have one element and then
# the sum will be equal to the one element value provided that is equal to the target sum
# we will work out the solution from top to bottom one row at a time, and one column at a time from right to left
# the final sum will be the bottom right cell
# if the sum is equal to sum(S)/2 then yes we found a subset, otherwise we didn't

def ES_1(S):

    # if 's' is a an odd number, we can't have two subsets with same total
    if sum(S) % 2 != 0:
        return False

    # Initialization
    T = [[0 for i in range(int(sum(S) / 2) + 1)] for j in range(len(S) + 1)]

    n = len(S)
    S = [0] + S  # Counting for the case of empty set of numbers

    # process all subsets for all sums
    for i in range(1, n + 1):
        for j in range(1, int(sum(S) / 2) + 1):
            if S[i] <= j:
                T[i][j] = max(T[i - 1][j - S[i]] + S[i], T[i - 1][j])
            else:
                T[i][j] = T[i - 1][j]

    return (T[n][int(sum(S) / 2)] == int(sum(S) / 2))


# Refernce implementation
def ES_2(S):
    # if 's' is a an odd number, we can't have two subsets with same total
    if sum(S) % 2 != 0:
        return False

    dp = [[0 for x in range(int(sum(S) / 2) + 1)] for y in range(len(S))]

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for j in range(1, int(sum(S) / 2) + 1):
        if S[0] == j:  # j is the required sum
            dp[0][j] = S[0]

    # process all subsets for all sums
    for i in range(1, len(S)):
        for j in range(1, int(sum(S) / 2) + 1):

            if S[i] < j:
                dp[i][j] = max(dp[i - 1][j - S[i]] + S[i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # the bottom-right corner will have our answer.
    return (dp[len(S) - 1][int(sum(S) / 2)]==int(sum(S) / 2))

    # TODO Fix this implementaion, simpler
    # Here rather than trying to find a subset of maximum sum and check if it is equal to the half
    # of the total sum and then the other half is another subset that is equal to the first one
    # rather than doing that we choose to the check if we can add the number toward the sum/2
    # if yes we set the solution at i,j to True other wise we set it to False
    # def ES_3(S):
    #
    #     # if 's' is a an odd number, we can't have two subsets with same total
    #     if sum(S) % 2 != 0:
    #         return False
    #
    #     # Initialization
    #     T = [[False for i in range(int(sum(S) / 2) + 1)] for j in range(len(S) + 1)]
    #     n = len(S)
    #     S = [0] + S# Counting for the case of empty set of numbers
    #

    # process all subsets for all sums
    for i in range(1, n + 1):
        for j in range(1, int(sum(S) / 2) + 1):
            if S[i] <= j:
                T[i][j] = T[i - 1][j - S[i]]
            else:
                T[i][j] = T[i - 1][j]

    return (T[n][int(sum(S) / 2)])

def main():
    S = [1, 2, 3, 4]

    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if ES_1(S) == ES_2(S) else 'Fail', S, ES_2(S), ES_1(S)))
    S = [2, 2, 5, 2, 5]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if ES_1(S) == ES_2(S) else 'Fail', S, ES_2(S), ES_1(S)))

    S = [2, 3, 4, 6]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if ES_1(S) == ES_2(S) else 'Fail', S, ES_2(S), ES_1(S)))

if __name__ == '__main__':
    main()
