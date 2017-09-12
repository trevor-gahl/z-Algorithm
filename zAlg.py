#!/bin/bash/python
'''
*************************************************
***  CSCI-451 Fall 2017 Z-algorithm           ***
***  Treavor Gahl, David Schwehr, Cas Loftin  ***
***                                           ***
***  Utilizing Z-algorithm to search for a    ***
***  pattern in a string in linear time.      ***
***  Gets user input for string and pattern,  ***
***  returns number of matches and length of  ***
***  longest match.                           ***
*************************************************
'''


def zAlg(s):

    # build an array of z-values
    Z = [0] * len(s)
    Z[0] = 0

    # initialize the right and left pointers
    rt = 0
    lt = 0

    # If the z box is to the left of your current index, explicitly compare
    for x in range(1, len(s)):
        if x > rt:
            n = 0
            while n + x < len(s) and s[n] == s[n + x]:
                n += 1
            Z[x] = n
            if n > 0:
                lt = x
                rt = x + n + 1
        else:
            p = x - lt
            right_part_len = rt - x + 1
            # If the length is entirely contained in the z box
            if Z[p] < right_part_len:
                Z[x] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - x]:
                    i += 1
                Z[x] = i - x

                lt = x
                rt = i - 1
    return Z


def exactMatch(p, t):
    patternLength = len(p)
    # print(patternLength)
    sentinel = ['$']
    maxMatch = 0
    match = 0
    test = p + sentinel + t
    print(test)
    zOut = z_advanced(test)
    print(zOut)
    # print(len(zOut))
    for i in range(len(zOut)):
        # print(patternLength - 1)
        if i < patternLength:
            continue
        else:
            # print(zOut[i])
            if zOut[i] == patternLength:
                # print("bem")
                match = match + 1
            else:
                if zOut[i] > maxMatch:
                    maxMatch += zOut[i]
    if match > 1:
        maxMatch = patternLength
    return match, maxMatch


def z_advanced(s):
    """An advanced computation of Z-values of a string."""

    Z = [0] * len(s)
    Z[0] = len(s)

    rt = 0
    lt = 0

    for k in range(1, len(s)):
        if k > rt:
            # If k is outside the current Z-box, do naive computation.
            n = 0
            while n + k < len(s) and s[n] == s[n + k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k + n - 1
        else:
            # If k is inside the current Z-box, consider two cases.

            p = k - lt  # Pair index.
            right_part_len = rt - k + 1

            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k

                lt = k
                rt = i - 1
    return Z


def main():
    sequence = input("Enter string, S, no spaces: \n")
    pattern = input(
        "Enter pattern, P, that you want to find matches in string: \n")
    sequenceList = list(sequence)
    patternList = list(pattern)
    print(sequenceList)
    print(patternList)
    zValues = z_advanced(sequenceList)
    print("Z-values: " + str(zValues))
    # print(zValues)
    matches = exactMatch(patternList, sequenceList)
    print(matches)
    print("Number of matches: " + str(matches[0]))
    print("Longest match: " + str(matches[1]))


'''
t = ['x', 'a', 'a', 'a', 'x', 'a', 'b', 'y']
testRun = zAlg(t)
print(testRun)
t2 = ['x', 'a', 'a']

print(exactMatch(t2, t))
'''
if __name__ == "__main__":
    main()
