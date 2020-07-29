# Given a stair with ‘n’ steps, implement a method to count how many
# possible ways are there to reach the top of the staircase,
# given that, at every step you can either take 1 step, 2 steps, or 3 steps.
# Fib Pattern

def CS(S):
    T = [0 for i in range(S + 1)]
    T[0] = 1
    T[1] = 1
    T[2] = 2

    for i in range(3, S + 1):
        T[i] = T[i - 1] + T[i - 2] + T[i - 3]

    return T[S]


def main():
    S = 3
    print("Testcase 1 is {0} for a stairs of {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CS(S) == 4 else 'Fail', S, CS(S), '4'))

    S = 4
    print("Testcase 1 is {0} for a stairs of {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CS(S) == 7 else 'Fail', S, CS(S), '7'))

    S = 5
    print("Testcase 1 is {0} for a stairs of {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CS(S) == 13 else 'Fail', S, CS(S), '13'))


if __name__ == '__main__':
    main()
