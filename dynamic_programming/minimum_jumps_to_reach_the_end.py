# Given an array of positive numbers, where each element represents
# the max number of steps that can be made forward from that element,
# considering all possible different steps we can take (starting from the first element)
# we want to find the minimum number of jumps  to reach the last position of the array
# that is position n-1 ( a jump is one or more steps ex:
# if at position 2 of the array there is value of 3 then we take one jump of one step
# one jump of two steps or one jump of three steps. )
# If an element is 0, then we cannot move through that element.
# Fib Pattern, I can also classify it as LIS pattern
import math
def CMJ(jumps):
    # Ini
    T = [math.inf for i in range(len(jumps))]
    # Base case
    T[0] = 0
    for i in range(len(jumps)):
        for j in range(i + 1, len(jumps)):
            # Increment the number of jumps if
            # current end point is within the range of the jumps
            if j <= (i + jumps[i]):
                T[j] = min(T[j], T[i] + 1)
    return T[-1]


# Reference implementation
def count_min_jumps(jumps):
    n = len(jumps)
    # initialize with infinity, except the first index which should be zero as we
    # start from there
    dp = [math.inf for _ in range(n)]
    dp[0] = 0

    for start in range(n - 1):
        end = start + 1
        while end <= start + jumps[start] and end < n:
            dp[end] = min(dp[end], dp[start] + 1)
            end += 1

    return dp[n - 1]
def main():
    jumps = [2, 1, 1, 1, 4]
    print("Testcase 1 is {0}, minimum number of jumps to reach the end for the set of jumps {1} "
          "is calculated: {2} while it should be {3}"
          .format('Pass' if CMJ(jumps) == count_min_jumps(jumps) else 'Fail', jumps,
                  CMJ(jumps), count_min_jumps(jumps)))

    jumps = [1, 1, 3, 6, 9, 3, 0, 1, 3]
    print("Testcase 1 is {0}, minimum number of jumps to reach the end for the set of jumps {1} "
          "is calculated: {2} while it should be {3}"
          .format('Pass' if CMJ(jumps) == count_min_jumps(jumps) else 'Fail', jumps,
                  CMJ(jumps), count_min_jumps(jumps)))

if __name__ == '__main__':
    main()
