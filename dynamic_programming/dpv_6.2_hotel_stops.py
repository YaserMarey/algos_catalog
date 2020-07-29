# DPV 6.2
# # You are going on a long trip. You start on the road at mile post 0. Along the way there are n
# # hotels, at mile posts a1 < a2 < · · · < an, where each ai is measured from the starting point. The
# # only places you are allowed to stop are at these hotels, but you can choose which of the hotels
# # you stop at. You must stop at the final hotel (at distance an), which is your destination.
# # You’d ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing
# # of the hotels). If you travel x miles during a day, the penalty for that day is (200 − x)^2.
#
# # You want
# # to plan your trip so as to minimize the total penalty—that is, the sum, over all travel days, of the
# # daily penalties.
# # Give an efficient algorithm that determines the optimal sequence of hotels at which to stop.
#
# # relation:
# # penalty[i] = minimum penalty to get to hotel i
# # penalty[i] = min([penalty[j] + (200 - (hotel[i] - hotel[j]))**2 for j in range(0, i) where hotel[i] - hotel[j] <= 200)
# # solution: penalty[-1]
# Longest increasing subsquence pattern

def minPenalty(d):
    l = [0]
    for i in range(1, len(d) + 1):
        l.append((200 - d[i - 1]) ** 2)
        for j in range(1, i):
            prev_stop = d[i - 1 - j]
            curr_stop = d[i - 1]
            penalty = (200 - (curr_stop - prev_stop)) ** 2 + l[i - j]
            if penalty < l[i]:
                l[i] = penalty
    # print(l)
    return (l[-1])


import math


def HS_1(D):
    MP = [math.inf for i in range(len(D) + 1)]
    MP[0] = 0
    D = [0] + D
    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            MP[j] = min(MP[i] + (200 - (D[j] - D[i])) ** 2, MP[j])
    # print(MP)
    return MP[-1]


def main():
    D = [25, 50, 200, 300, 400]
    print("Testcase 1 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if HS_1(D) == minPenalty(D) else 'Fail', D, HS_1(D), minPenalty(D)))
    D = [25, 50, 200, 300, 350]
    print("Testcase 2 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if HS_1(D) == minPenalty(D) else 'Fail', D, HS_1(D), minPenalty(D)))

    D = [25, 50, 205, 300, 400]
    print("Testcase 3 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if HS_1(D) == minPenalty(D) else 'Fail', D, HS_1(D), minPenalty(D)))

    D = [25, 175, 200, 300, 500]
    print("Testcase 4 is {0} for array {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if HS_1(D) == minPenalty(D) else 'Fail', D, HS_1(D), minPenalty(D)))


if __name__ == '__main__':
    main()
