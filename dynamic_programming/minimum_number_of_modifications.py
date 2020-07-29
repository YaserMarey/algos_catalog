# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters.
# Write a function to calculate the count of the minimum number of deletion and insertion operations.
# Solution: We can finding the length of the Longest common subsequence and subtracting that form the the total length
# Longest common subsequence pattern

def LCS(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    maxLength = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            maxLength = max(maxLength, dp[i][j])

    return maxLength


# TODO I have another slightly different implemention for LCS but it raises exception wiht this, FIX it
def main():
    s1 = "abc"
    s2 = "fbc"
    c1 = LCS(s1, s2)
    print("Minimum deletions needed: " + str(len(s1) - c1))
    print("Minimum insertions needed: " + str(len(s2) - c1))

    s1 = "abdca"
    s2 = "cbda"
    c1 = LCS(s1, s2)
    print("Minimum deletions needed: " + str(len(s1) - c1))
    print("Minimum insertions needed: " + str(len(s2) - c1))
    #
    s1 = "passport"
    s2 = "ppsspt"
    c1 = LCS(s1, s2)
    print("Minimum deletions needed: " + str(len(s1) - c1))
    print("Minimum insertions needed: " + str(len(s2) - c1))

    # print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
    #       .format('Pass' if BS(A, 0, len(A) - 1, 3) == brute_force(A, 3) else 'Fail', A, BS(A, 0, len(A) - 1, 3),
    #               brute_force(A, 3)))


if __name__ == '__main__':
    main()
