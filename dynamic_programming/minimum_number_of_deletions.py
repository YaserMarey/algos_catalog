# Given a number sequence, find the minimum number of elements that should be
# deleted to make the remaining sequence sorted.
# Longest increasing subsequence pattern

import math


def MD(A):
    # Ini first, to create the matrix
    # Here we are looking for minimum, so we initialize T to infinity
    T = [math.inf for i in range(len(A))]
    # Base case, it requires only to delete the character at i = 0 if we have only one character
    # since an empty sequence is sorted
    T[0] = 1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):

            if A[j] < A[i]:
                # if we need to delete the current element of the sequence ot keep it sorted
                # then we need add one and choose the minimum
                T[j] = min(T[j], T[i] + 1)
            else:
                # otherwise carry the best result so far forward
                T[j] = T[i]
    return T[-1]


def lengthOfLIS(A):
    if len(A) == 0: return 0
    LIS = [1 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] > A[i]:
                LIS[j] = max(LIS[j], LIS[i] + 1)
    return max(LIS)


def main():
    A = [4, 2, 3, 6, 10, 1, 12]
    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if MD(A) == len(A) - lengthOfLIS(A) else 'Fail', A, MD(A), len(A) - lengthOfLIS(A)))
    A = [-4, 10, 3, 7, 15]

    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if MD(A) == len(A) - lengthOfLIS(A) else 'Fail', A, MD(A), len(A) - lengthOfLIS(A)))


if __name__ == '__main__':
    main()
