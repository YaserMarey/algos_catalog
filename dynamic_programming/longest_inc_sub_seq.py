# Longest increasing subsequence pattern
def S_1(A):
    LIS = [1 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(0,i):
            if A[i]>A[j]:
                LIS[i] = max(LIS[i],LIS[j] + 1)
    return max(LIS)

def S_2(A):
    LIS = [1 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] > A[i]:
                LIS[j] = max(LIS[j], LIS[i] + 1)
    return max(LIS)

def S_3(A):
    LIS = [1 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(0,i):
            if A[i]>A[j]:
                LIS[i] = max(LIS[i], LIS[j]+1)
    return max(LIS)


def S_4(A):
    LIS = [1 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] > A[i]:
                LIS[j] = max(LIS[j], LIS[i] + 1)
            # Carrying the best result so far forward
            # so that we don't need max(LIS) as we did in S_2
            else:
                LIS[j] = LIS[i]
    # just return the last character
    return LIS[-1]


def lengthOfLIS(A):
    if len(A) == 0: return 0
    LIS = [1 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] > A[i]:
                LIS[j] = max(LIS[j], LIS[i] + 1)
    return max(LIS)

def main():
    A = [15, 27, 14, 38, 26, 55, 46, 65, 12]

    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if S_2(A) == lengthOfLIS(A) else 'Fail', A, S_2(A), lengthOfLIS(A)))

    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if S_4(A) == lengthOfLIS(A) else 'Fail', A, S_4(A), lengthOfLIS(A)))

    A = [15, 27, 14, 38, 26, 55, 46, 65, 85]

    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if S_2(A) == lengthOfLIS(A) else 'Fail', A, S_2(A), lengthOfLIS(A)))

    print("Testcase 1 is {0} for sequence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if S_4(A) == lengthOfLIS(A) else 'Fail', A, S_4(A), lengthOfLIS(A)))

if __name__ == '__main__':
    main()
