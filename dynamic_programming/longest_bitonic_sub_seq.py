# Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS).
# A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

def LBS(A):
    TF = [1 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] > A[i]:
                TF[j] = max(TF[j], TF[i] + 1)

    TB = [1 for i in range(len(A))]
    for i in range(len(A) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if A[j] > A[i]:
                TB[j] = max(TB[j], TB[i] + 1)

    maxLength = 0
    for i in range(len(A)):
        maxLength = max(maxLength, TF[i] + TB[i])
    # print(TF)
    # print(TB)
    return maxLength


# Anohter implementation to verify against
def find_LBS_length(nums):
    n = len(nums)
    lds = [0 for _ in range(n)]
    ldsReverse = [0 for _ in range(n)]

    # find LDS for every index up to the beginning of the array
    for i in range(n):
        lds[i] = 1  # every element is an LDS of length 1
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                lds[i] = max(lds[i], lds[j] + 1)

    # find LDS for every index up to the end of the array
    for i in range(n - 1, -1, -1):
        ldsReverse[i] = 1  # every element is an LDS of length 1
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                ldsReverse[i] = max(ldsReverse[i], ldsReverse[j] + 1)

    maxLength = 0
    for i in range(n):
        maxLength = max(maxLength, lds[i] + ldsReverse[i])
    # print(lds)
    # print(ldsReverse)
    return maxLength


def main():
    A = [4, 2, 3, 6, 10, 1, 12]
    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if LBS(A) == find_LBS_length(A) else 'Fail', A, LBS(A), find_LBS_length(A)))

    A = [4, 2, 5, 9, 7, 6, 10, 3, 1]

    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if LBS(A) == find_LBS_length(A) else 'Fail', A, LBS(A), find_LBS_length(A)))


if __name__ == '__main__':
    main()
