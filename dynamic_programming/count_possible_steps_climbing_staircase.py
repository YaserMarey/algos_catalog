# Given a stair with 'n' steps, implement a method to count how many possible ways are there to reach the top of the staircase,
# given that, at every step you can either take 1 step, 2 steps, or 3 steps.
# Fibonacci Numbers Pattern
# From the first sight it looks very similar to Coin Change Problem - Unbounded KS Pattern
# But there is a slight difference, that is for coin change a coin set {1,2} and {2,1} are counted as one set
# where for stair case problem there are counted as two different sets, that is we can take one step and then two
# and that is different than taking two steps frist and then one
# Fib Pattern

def CSC(Length):
    dp = [0 for _ in range(Length + 1)]
    dp[0] = 1  # if stairs length = 0 then there is only way to climb the stairs which is taking no steps
    dp[1] = 1  # if stairs length = 1 then there is one way to climb the stairs that is to take one step
    dp[2] = 2  # if stairs length = 2 then there is two ways to climb the stais that is to either {1,1}, {2}

    # Now starting from third step, until the end we calculate the number of possible sets of steps
    # by summing the count of the possible sets of steps
    for i in range(3, Length + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[Length]


def main():
    Stpes = [1, 2, 3]
    Length = 3
    print(" Staris length {0}, possible jumps {1}, Test case {2} "
          "since it has calculated possible set of steps to {3} {4}"
          .format(Length, Stpes, 'Pass' if CSC(Length) == 4 else 'Fail', CSC(Length), ' and it is 4'))

    Length = 4
    print(" Staris length {0}, possible jumps {1}, Test case {2} "
          "since it has calculated possible set of steps to {3} {4}"
          .format(Length, Stpes, 'Pass' if CSC(Length) == 7 else 'Fail', CSC(Length), ' and it is 7'))

    Length = 5
    print(" Staris length {0}, possible jumps {1}, Test case {2} "
          "since it has calculated possible set of steps to {3} {4}"
          .format(Length, Stpes, 'Pass' if CSC(Length) == 13 else 'Fail', CSC(Length), ' and it is 13'))


if __name__ == '__main__':
    main()
