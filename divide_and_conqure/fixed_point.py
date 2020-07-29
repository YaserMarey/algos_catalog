# Given a sorted array of n distinct integers A = {a1, a2, ..., an}
# Find out whether there is an index i for which ai = i.
# Give a divide and conquer algorithm to solve this problems that runs
# in time O(log(n)).
# DPV 2.17
# From 'Algorithms', by S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani, 2006.


def FFP(A, left, right):
    mid = (left + right) // 2
    if (left == right):
            return A[mid] == mid
    if A[mid] == mid:
        return True
    elif A[mid] > mid: #look into left subarray
        return FFP(A, left, mid)
    else: #look into right subarray
        return FFP(A, mid+1, right)

def brute_force(A):
    for i in range(len(A)):
        if A[i]==i:
            return True
    return False

def main():
    A = [1, 2, 3, 4, 5, 6, 7]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if FFP(A, 0, len(A)-1) == brute_force(A) else 'Fail', A, FFP(A, 0, len(A)-1), brute_force(A)))

    A = [-2, 0, 2, 5, 7, 8, 10]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if FFP(A, 0, len(A)-1) == brute_force(A) else 'Fail', A, FFP(A, 0, len(A)-1), brute_force(A)))

    A = [-5, 0, 1 , 3]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if FFP(A, 0, len(A)-1) == brute_force(A) else 'Fail', A, FFP(A, 0, len(A)-1), brute_force(A)))

    A = [-5, 0, 1 , 3]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if FFP(A, 0, len(A)-1) == brute_force(A) else 'Fail', A, FFP(A, 0, len(A)-1), brute_force(A)))

    A = [0, 5, 6]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if FFP(A, 0, len(A)-1) == brute_force(A) else 'Fail', A, FFP(A, 0, len(A)-1), brute_force(A)))

if __name__ == '__main__':
    main()
