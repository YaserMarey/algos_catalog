# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums..
# 0/1 Knapsack Pattern
# We are trying to find a subset whose sum is as close to 'S/2' as possible,
# because if we can partition the given set into two subsets of an equal sum,
# we get the minimum difference i.e. zero. This transforms our problem to Subset Sum
# So if we are trying to find a subset of given numbers that has a total sum of 's/2'.
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
# the final sum will be the bottom right cell which will be the closest sum to S/2 and therefore its abs difference
# from S/2 is the minimum

# Reference implementation
def minimum_difference(S):

    # if 's' is a an odd number, we can't have two subsets with same total
    if sum(S) % 2 != 0:
        return False

    dp = [[0 for x in range(int(sum(S) / 2) + 1)] for y in range(len(S))]

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for j in range(1, int(sum(S) / 2) + 1):
        if S[0] == j: # j is the required sum
            dp[0][j] = S[0]

    # process all subsets for all sums
    for i in range(1, len(S)):
        for j in range(1, int(sum(S) / 2) + 1):

            if S[i] < j:
                dp[i][j] = max(dp[i - 1][j - S[i]] + S[i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # the bottom-right corner will have our answer.
    # print (dp)
    # print (int(sum(S)/2))
    return abs((dp[len(S) - 1][int(sum(S) / 2)] - int(sum(S) / 2)))


def MD(S):
    C = int(sum(S) / 2)
    T = [[0 for j in range(C + 1)] for i in range(len(S) + 1)]

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
    return abs((T[n][int(sum(S) / 2)] - int(sum(S) / 2)))


def main():
    S = [1, 2, 3, 4]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if MD(S) == minimum_difference(S) else 'Fail', S, MD(S), minimum_difference(S)))

    S = [1, 1, 3, 4, 7]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if MD(S) == minimum_difference(S) else 'Fail', S, MD(S), minimum_difference(S)))

    S = [2, 2, 4, 6]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if MD(S) == minimum_difference(S) else 'Fail', S, MD(S), minimum_difference(S)))

if __name__ == '__main__':
    main()
