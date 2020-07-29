# Modified Binary Search to find closest integer for an element in an array
# time complexity is O(nlogn)

import math

from divide_and_conqure.merge_sort import merge_sort


def Find_Closest(A, B):
    # We are looking into B therefore we sort it
    # A is just a sequence of numbers that we will search he closest
    # to one number at a time

    B = merge_sort(B)
    C = []
    for a in A:
        C.append(BS_Closest(B, 0, len(B) - 1, a))
    return C


def BS_Closest(B, left, right, a):
    mid = (left + right) // 2  # // Floors result
    if left == right:
        return B[mid]
    if B[mid] == a:
        return B[mid]

    if right - left == 1:
        if abs(B[left] - a) < abs(B[right] - a):
            return B[left]
        else:
            return B[right]

    if B[mid] > a:  # look into left subarray
        return BS_Closest(B, left, mid, a)
    else:
        # look into right subarray
        # notice mid is missing '+1' that exists in my implementation for binary
        # search in binary_search.py, the reason is that we want to look for
        # the closest match, and therefore we want to handle the case of
        # 2 elements, rather than jump from 3 to 1 element and we are
        # handling this case above ( right - left == 1 )
        return BS_Closest(B, mid, right, a)


def brute_force(A, B):
    C = []
    for i in range(len(A)):
        minimum = math.inf
        for j in range(len(B)):
            if abs(A[i] - B[j]) <= minimum:
                minimum = abs(A[i] - B[j])
                c = B[j]
        C.append(c)
    return C


def main():
    A = [6, 1, 12]
    B = [1, 3, 10]
    print("Testcase 1 is {0} for A {1} and B {2} since it is calculated as {3} and it should be {4}"
          .format('Pass' if Find_Closest(A, B) == brute_force(A, B) else 'Fail', A, B, Find_Closest(A, B),
                  brute_force(A, B)))

    A = [6, 1, 12]
    B = [1, 0, 8]

    print("Testcase 2 is {0} for A {1} and B {2} since it is calculated as {3} and it should be {4}"
          .format('Pass' if Find_Closest(A, B) == brute_force(A, B) else 'Fail', A, B, Find_Closest(A, B),
                  brute_force(A, B)))


if __name__ == '__main__':
    main()
