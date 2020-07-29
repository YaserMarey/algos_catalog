# DPV 6.11
# Given two strings x = x1x2 ... xn and y = y1y2 ... ym, we wish to find the length of their longest
# common subsequence, that is, the largest k for which there are indices i1 < i2 < ... < ik and
# j1 < j2 < ... < jk with xi1xi2 ... xik = yj1yj2 ... yjk . Show how to do this in time O(mn).
# LCS pattern
def LCS(X, Y):
    L = [[0 for i in range(len(X))] for j in range(len(Y))]
    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i]==Y[j]:
                L[i][j] = 1 + L[i - 1][j - 1]
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[len(X) - 1][len(Y) - 1]

def main():
    X = ['B','C','D','B','C','D','A']
    Y = ['A', 'B', 'E', 'C', 'B', 'A', 'B']

    print("Testcase 1 is {0} for string {1}, and {2} since it is calculated as {3} and it should be {4}"
          .format('Pass' if LCS(X, Y) == 4 else 'Fail', X, Y, LCS(X, Y), '4'))

if __name__ == '__main__':
    main()
