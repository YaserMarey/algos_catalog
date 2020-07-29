# There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses.
# The only restriction the thief has is that he can’t steal from two consecutive houses,
# as that would alert the security system. How should the thief maximize his stealing?

# Reference implementation
def find_max_steal(wealth):
    n = len(wealth)
    if n == 0:
        return 0
    dp = [0 for x in range(n + 1)]  # '+1' to handle the zero house
    dp[0] = 0  # if there are no houses, the thief can't steal anything
    dp[1] = wealth[0]  # only one house, so the thief have to steal from it

    # please note that dp[] has one extra element to handle zero house
    for i in range(1, n):
        dp[i + 1] = max(wealth[i] + dp[i - 1], dp[i])

    return dp[n]


#
def HT_(S):
    # ini
    T = [0 for i in range(len(S))]
    # basecase
    T = T + [0]  # additional element, profit is zero if we still no house
    T[1] = S[0]

    for i in range(1, len(S)):
        # you have two options either to steal or not at each house i
        # if no steal then profit of next house profit is only the current profit T[i]
        # if you decide to steal then the next house profit is prev profit in addtion the steal of this house S[i]
        T[i + 1] = max(T[i], T[i - 1] + S[i])
    return T[-1]


# Easire to understand but not passing all test cases
def HT(S):
    # ini
    T = [0 for i in range(len(S))]
    # basecase
    T = T + [0]  # additional element, profit is zero if we still no house
    # The profit of the first house is the maximum of the profits of first house and the second house
    T[1] = max(S[0], S[1])

    # Now starting from the second
    for i in range(3, len(S)):
        # you have two options either to steal or not at each house i
        # if you steal then profit of house  i is the profit of house before last one T[i-2] + current S[i]
        # if no steal then the profit is what you have from last only that is T[i-1]
        T[i] = max(T[i - 2] + S[i], T[i - 1])
    return T[-2]


def main():
    S = [2, 5, 1, 3, 6, 2, 4]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if HT(S) == find_max_steal(S) else 'Fail', S, HT(S), find_max_steal(S)))

    S = [2, 10, 14, 8, 1]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if HT(S) == find_max_steal(S) else 'Fail', S, HT(S), find_max_steal(S)))

    S = [1, 2, 3, 1]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if HT(S) == find_max_steal(S) else 'Fail', S, HT(S), find_max_steal(S)))


if __name__ == '__main__':
    main()
