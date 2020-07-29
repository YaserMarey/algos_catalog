# Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
# In a palindromic subsequence, elements read the same backward and forward.


# Reference implementation
def find_LPS_length(st):
    n = len(st)
    # dp[i][j] stores the length of LPS from index 'i' to index 'j'
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # every sequence with one element is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            # case 1: elements at the beginning and the end are the same
            if st[startIndex] == st[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:  # case 2: skip one element either from the beginning or the end
                dp[startIndex][endIndex] = max(
                    dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

    return dp[0][n - 1]


# TODO this is similar to above implementation, it fills the solution matrics
# TODO row by row, fix this to fill column by column or try to fill it
# TODO such that the counters start from the begining of the sequence rather than the end

# def LPS(A):
#     # Ini: dp[i][j] stores the length of LPS from index 'i' to index 'j'
#     dp = [[0 for j in range(len(A))] for i in range(len(A))]
#
#     n = len(A)
#     # Base case: every sequence with one element is a palindrome of length 1
#     for i in range(n): dp[i][i] = 1
#
#     for i in range(n - 1, -1, -1):
#         for j in range(i + 1, n):
#             # print("i,j is ({0},{1})".format(i, j))
#             # case 1: elements at the beginning and the end are the same
#             if A[i] == A[j]:
#                 dp[i][j] = 2 + dp[i + 1][j - 1]
#             else:  # case 2: skip one element either from the beginning or the end
#                 dp[i][j] = max(
#                     dp[i + 1][j], dp[i][j - 1])
#
#     return dp[0][len(A) - 1]

def LPS(A):
    # Ini: dp[i][j] stores the length of LPS from index 'i' to index 'j'
    dp = [[0 for j in range(len(A))] for i in range(len(A))]

    n = len(A)
    # Base case: every sequence with one element is a palindrome of length 1
    for i in range(n): dp[i][i] = 1

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            # case 1: elements at the beginning and the end are the same
            if A[i] == A[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:  # case 2: skip one element either from the beginning or the end
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def main():
    A = "abdbca"
    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if LPS(A) == find_LPS_length(A) else 'Fail', A, LPS(A), find_LPS_length(A)))


if __name__ == '__main__':
    main()
