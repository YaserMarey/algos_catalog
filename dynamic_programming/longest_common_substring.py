# LCS Pattern
# Given string A of length n and string B of length m
# Find the length of the longest common substring between the two strings A, B
# Notice that substring means no gabs

def LCS_1(A, B):
    dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
    maxLength = 0
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            if A[i] == B[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                maxLength = max(maxLength, dp[i][j])
            else:
                dp[i][j] = 0
    return maxLength


def main():
    X = 'passport'
    Y = 'ppsspt'
    print("Testcase 1 is {0} for array {1}, and {2} since it is calculated as {3} and it should be {4}"
          .format('Pass' if LCS_1(X, Y) == 3 else 'Fail', X, Y, LCS_1(X, Y), '3'))

    X = "abdca"
    Y = "cbda"
    print("Testcase 2 is {0} for array {1}, and {2} since it is calculated as {3} and it should be {4}"
          .format('Pass' if LCS_1(X, Y) == 2 else 'Fail', X, Y, LCS_1(X, Y), '2'))


if __name__ == '__main__':
    main()
