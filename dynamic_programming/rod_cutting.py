# A Dynamic Programming solution for Rod cutting problem
# Unbounded supply Knapsack pattern

# Reference implementation
def rod_cutting(Prices, Cuts, Length):
    T = [[0 for j in range(Length + 1)] for i in range(len(Prices))]
    for i in range(0, len(Prices)):
        for j in range(1, Length + 1):
            if Cuts[i] <= j:
                T[i][j] = max(Prices[i] + T[i][j - Cuts[i]], T[i - 1][j])
            else:
                T[i][j] = T[i - 1][j]
    return T[len(Prices) - 1][Length]


# P is profites, C is Cuts, and L is length of the rod
def RC(P, C, L):
    T = [[0 for j in range(L + 1)] for i in range(len(P) + 1)]

    n = len(C)

    C = [0] + C
    P = [0] + P

    for i in range(1, n + 1):
        for j in range(1, L + 1):
            if C[i] <= j:
                T[i][j] = max(P[i] + T[i][j - C[i]], T[i - 1][j])
            else:
                T[i][j] = T[i - 1][j]
    return T[n][L]


def main():
    Prices = [2, 6, 7, 10, 13]
    Cuts = [1, 2, 3, 4, 5]
    Length = 5
    print('Test case 1: {0} maximum KS value is calculated as {1}'.format('Pass'
                                                                          if RC(Prices, Cuts, Length) == rod_cutting(
        Prices, Cuts, Length)
                                                                          else 'Fail', RC(Prices, Cuts, Length)))


if __name__ == '__main__':
    main()
