# Given a number 'n'
# Count how many possible ways there are to express 'n' as the sum of 1, 3, or 4.
# Notice that {1,2} and {2,1} are two methods and not counted as one
# Pattern Fibonacci Number


def CFS(Number):
    dp = [0 for _ in range(Number + 1)]
    dp[0] = 1  # if number = 0 then there is only set of factors which the empty set
    dp[1] = 1  # if number = 1 then there is only set of factors {1}
    dp[2] = 1  # if number = 2 then there is only set of factors {1,1}
    dp[3] = 2  # if number = 2 then there is only set of factors {1,1,1} & {3}

    # Now starting from third step, until the end we calculate the number of possible sets of steps
    # by summing the count of the possible sets of steps
    for i in range(4, Number + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]
    return dp[Number]


def main():
    Number = 4
    print(" Number {0}, possible factors 1,3,4 , Test case {1} "
          "since it has calculated possible set of factors to {2} {3}"
          .format(Number, 'Pass' if CFS(Number) == 4 else 'Fail', CFS(Number), ' and it is 4'))

    Number = 6
    print(" Number {0}, possible factors 1,3,4 , Test case {1} "
          "since it has calculated possible set of factors to {2} {3}"
          .format(Number, 'Pass' if CFS(Number) == 9 else 'Fail', CFS(Number), ' and it is 9'))


if __name__ == '__main__':
    main()
