# DPV 6.1
# Given an input sequence a1,a2...an
# Find the maximum sum of contiguous sub-sequence


def M_1(A):
    MS = [0 for i in range(len(A))]
    for i in range(1, len(A)):
        if MS[i] < (MS[i - 1] + A[i]):
                MS[i] = MS[i-1] + A[i]
        else:
            MS[i] = 0
    return max(MS)

def main():
    A = [5, 15, -30, 10, -5, 40, 10]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if M_1(A) == 55 else 'Fail', A, M_1(A), '55'))

if __name__ == '__main__':
    main()
