# Given a sorted array of n integers find if given elements exists
# A simple approach is to do linear search which is O(n)
# Recurrence of Binary search is T(N/2) + O(1), a=1, b=2, d=0 and log a base b = 0, then since
# log a base b = d = 0 recurrence becomes n power d times log n = logn

def BS(A, left, right, b):
    mid = (left + right) // 2
    if left == right:
        return A[mid] == b
    if A[mid] == b:
        return True
    elif A[mid] > b:  # look into left sub-array
        return BS(A, left, mid, b)
    else:  # look into right sub-array
        return BS(A, mid+1, right, b)


def brute_force(A, b):
    for i in range(len(A)):
        if A[i] == b:
            return True
    return False

def main():
    A = [1, 2, 3, 4, 5, 6, 7]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if BS(A, 0, len(A) - 1, 3) == brute_force(A, 3) else 'Fail', A, BS(A, 0, len(A) - 1, 3),
                  brute_force(A, 3)))

    A = [-2, 0, 2, 5, 7, 8, 10]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if BS(A, 0, len(A) - 1, 9) == brute_force(A, 9) else 'Fail', A, BS(A, 0, len(A) - 1, 9),
                  brute_force(A, 9)))

    A = [-5, 0, 1, 3]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if BS(A, 0, len(A) - 1, -5) == brute_force(A, -5) else 'Fail', A, BS(A, 0, len(A) - 1, -5),
                  brute_force(A, -5)))

    A = [0, 5, 6]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if BS(A, 0, len(A) - 1, 6) == brute_force(A, 6) else 'Fail', A, BS(A, 0, len(A) - 1, 6),
                  brute_force(A, 6)))


if __name__ == '__main__':
    main()
