# Given string S1 and string S2.
# Find the minimum number of operations to convert S1 to S2.
# Operations can be either delete, insert or replace a character in S2
# the cost of delete is 1, insert 1 while replace is 2
# Longest common substring pattern, I tend to put this into a catebory by itself, we may call it
# Edit Distance Patten, in this category we have problems such as sequence alignment and its variations

def MED(S1, S2):
    n, m = len(S1), len(S2)

    # Create dp matrices
    dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]

    # Base case,
    # if S2 is has no characters, then we need at each ith position of S1
    # to delete the jthe character and therefore distance at dp[i][0] is i operations
    for i in range(n + 1):
        dp[i][0] = i

    # if S1 is has no characters, then we need at each jth position of S2
    # to insert the jth character and therefore distance at dp[0][j] is j operations
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,  # delete
                               dp[i][j - 1] + 1,  # insert
                               dp[i - 1][j - 1] + 2)  # replace

    return dp[n][m]

def main():
    print("Testcase 1 is {0}, minimum edit distance for two strings {1} , {2} is calculated: {3}"
          .format('Pass' if MED("bat", "but") == 2 else 'Fail', "bat", "but", MED("bat", "but")))

    print("Testcase 1 is {0}, minimum edit distance for two strings {1} , {2} is calculated: {3}"
          .format('Pass' if MED("abdca", "cbda") == 3 else 'Fail', "abdca", "cbda", MED("abdca", "cbda")))

    print("Testcase 1 is {0}, minimum edit distance for two strings {1} , {2} is calculated: {3}"
          .format('Pass' if MED("passpot", "ppsspqrt") == 5 else 'Fail', "passpot", "ppsspqrt",
                  MED("passpot", "ppsspqrt")))

if __name__ == '__main__':
    main()
