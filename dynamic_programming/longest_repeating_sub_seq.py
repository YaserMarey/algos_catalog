def find_LRS_length(str):
    n = len(str)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    maxLength = 0
    # dp[i1][i2] will be storing the LRS up to str[0..i1-1][0..i2-1]
    # this also means that subsequences of length zero(first row and column of
    # dp[][]), will always have LRS of size zero.
    for i1 in range(1, n + 1):
        for i2 in range(1, n + 1):
            if i1 != i2 and str[i1 - 1] == str[i2 - 1]:
                dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
            else:
                dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
            maxLength = max(maxLength, dp[i1][i2])
    # print (dp)
    return maxLength


# TODO Fix
# The following is possibly not a correct implementatioin it should be similar to
# LCS except it tries to find common subsequnce between the the sequence and its replica
# and we should not consider it a match if the index of the character is the same

def LRS(A):
    T = [1 for i in range(len(A))]
    # T = [0]+T
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] == A[i]:
                T[j] = max(T[j], T[i] + 1)
            # Carrying the best result so far forward
            # so that we don't need max(LIS) as we did in S_2
            else:
                T[j] = T[i]
    # just return the last character
    print(T)
    return T[-1]


def main():
    # print(find_LRS_length("tomorrow"))
    # print(find_LRS_length("aabdbcec"))
    print(find_LRS_length("abcabcabc"))
    # print(find_LRS_length("fmff"))

    # print(LRS("tomorrow"))
    # print(LRS("aabdbcec"))
    print(LRS("abcabcabc"))
    # print(LRS("fmff"))


main()
