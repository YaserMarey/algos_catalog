# Given a no punctionaton string of n chdarcters
# Check if you can reconstruct it as sequnce of valid words
# This algorithm should take at most O(n2) time.
# You have a dictionary data strucutre that contains the set of valid words
# checking if a sequce of charcters is a valid word is one step operation.
# If the string is valid, output the sequence of words.
# DPV 6.4
# Longest increasing subseuqnce pattern

from collections import defaultdict


def reconstruct_sentence(s, d):
    n = len(s) + 1
    t = [False] * n
    next_word_idx = [0] * n

    # Base case
    t[0] = True

    # Recurrence
    for i in range(1, n):
        t[i] = False
        for j in range(1, i + 1):
            # i and j correspond to our memoization array t
            # which contains an extra element to represent the
            # empty substring. We must adjust them to work with
            # the s character array.
            si = i - 1
            sj = j - 1

            substr = "".join(s[sj:si + 1])

            if d[substr] and t[j - 1]:
                t[i] = True
                next_word_idx[j - 1] = i

    # print("The string s contains a valid sentence:")
    # print(t)
    # print(t[n-1])
    return t[n - 1]


def CS(s, d):
    T = [False for i in range(len(s))]
    T = [True] + T
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if T[i] and d["".join(s[i:j])]:
                T[j] = True
    # print(T)
    # No need to check other words, since T[-1] will be true only
    # if the rest of the words are reconstructed and the last word as well
    # is reconstructed correctly.
    return T[-1]


def main():
    full_sentence = "you are a bold one"
    split_sentence = full_sentence.split(" ")
    s = list("".join(split_sentence))  # e.g. 'youareaboldone'

    starter_words = {
        "it": True,
        "was": True,
        "the": True,
        "he": True,
        "best": True,
        "to": True,
        "of": True,
        "times": True,
        "time": True,
        "twas": True
    }

    d = defaultdict(bool, starter_words)

    # Add in the words from our sentence
    # to the dictionary
    for word in split_sentence:
        d[word] = True

    CS(s, d)
    reconstruct_sentence(s, d)

    print("Testcase 1 is {0} for sentence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CS(s, d) == reconstruct_sentence(s, d) else 'Fail', full_sentence, CS(s, d),
                  reconstruct_sentence(s, d)))

    full_sentence = 'yyouareaboldone'

    print("Testcase 1 is {0} for sentence {1}, since it is calculated as {2} and it should be {3}"
          .format('Pass' if CS(full_sentence, d) == reconstruct_sentence(full_sentence, d) else 'Fail', full_sentence,
                  CS(s, d),
                  reconstruct_sentence(full_sentence, d)))


if __name__ == '__main__':
    main()
