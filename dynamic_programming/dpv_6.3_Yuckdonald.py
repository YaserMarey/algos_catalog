# DPV 6.3 Yuckdonald's is opening restaurants along a strip of highway. You are given the distances from the starting
# point of the possible locations of the highways and the profits at each of these locations. You can only
# have one restaurant at each location and each location must be at least (k) miles apart.
# Longest increasing subsequnce pattern
def yuckdonald(miles, profits, k):
    n = len(miles)
    T = [None] * n
    for i in range(n):
        T[i] = profits[i]
        for j in range(i):
            if miles[i] - miles[j] >= k:
                T[i] = max(T[i], T[j] + profits[i])
    # print(T)
    return T[n - 1]


def YK(D, P, k):
    # Base case, maximum profit achieved at opening only the first resturant
    #  equals to the profit that resturant only other wise all Maximum profit is initialzed to zero

    MP = [0 for i in range(len(D))]
    MP[0] = P[0]

    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            if (D[j] - D[i]) >= k:
                MP[j] = max(MP[j], MP[i] + P[j])
    # print(MP)
    return MP[-1]


def main():
    k = 5
    distance = [1, 4, 9, 16]
    profit = [10, 5, 10, 20]

    print("Testcase 1 is {0} for Distances {1}, and Profits {2} and k = {3}, since minimum profit is calculated as {4} "
          "and it should be {5}"
          .format('Pass' if YK(distance, profit, k) == yuckdonald(distance, profit, k) else 'Fail', distance, profit, k,
                  YK(distance, profit, k),
                  yuckdonald(distance, profit, k)))

    distance = [1, 2, 3, 4, 5, 6]
    profit = [1, 2, 3, 4, 5, 6]
    print("Testcase 1 is {0} for Distances {1}, and Profits {2} and k = {3}, since minimum profit is calculated as {4} "
          "and it should be {5}"
          .format('Pass' if YK(distance, profit, k) == yuckdonald(distance, profit, k) else 'Fail', distance, profit, k,
                  YK(distance, profit, k),
                  yuckdonald(distance, profit, k)))

    distance = [1]
    profit = [222]

    print("Testcase 1 is {0} for Distances {1}, and Profits {2} and k = {3}, since minimum profit is calculated as {4} "
          "and it should be {5}"
          .format('Pass' if YK(distance, profit, k) == yuckdonald(distance, profit, k) else 'Fail', distance, profit, k,
                  YK(distance, profit, k),
                  yuckdonald(distance, profit, k)))


if __name__ == '__main__':
    main()
