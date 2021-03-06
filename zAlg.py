#!/bin/bash/python3
'''
**********************************************************************************
***  CSCI-451 Fall 2017 Z-algorithm                                            ***
***  Treavor Gahl, David Schwehr, Cas Loftin                                   ***
***                                                                            ***
***  Adapted from Z-algorithm tutorial by                                      ***
***     Ivan Yurchenko @ https://ivanyu.me/blog/2013/10/15/z-algorithm/        ***
***                                                                            ***
***  Utilizing Z-algorithm to search for a pattern in a string in linear time. ***
***  If passing no command line arguments: user is promted for input for       ***
***  string and pattern. If you want to use a file with a sequence give the    ***
***  file path as a command line argument. The program returns number of       ***
***  matches and length of longest match.                                      ***
**********************************************************************************
'''

import sys


def createZTable(s):
    ''' createZTable() receives a string and returns a list of Z-values '''

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


def exactMatch(pattern, sequence):
    ''' exactMatch() receives a list for a pattern and a list for a sequence,
        will return number of matches and longest match. Number of matches will
        be any prefix of pattern found in sequence. Longest match will be the
        longest prefix of pattern found in sequence. If the longest match equals
        the length of pattern the entire pattern was found and numberOfMatches
        will be counted/incremented. '''

    patternLength = len(pattern)
    #print("pattern length: " + str(patternLength))
    sentinel = ['$']
    maxMatch = 0
    match = 0
    test = pattern + sentinel + sequence
    zValues = createZTable(test)

    for i in range(len(zValues)):
        if i < patternLength:
            continue
        else:
            if zValues[i] == patternLength:
                match = match + 1
            else:
                if zValues[i] > maxMatch:
                    maxMatch += zValues[i]
    if match > 0:
        maxMatch = patternLength

    return match, maxMatch


def main():
    
    if len(sys.argv) < 2:
        sequence = input("Enter string, S: \n")
        pattern = input("Enter pattern, P, that you want to find matches in string: \n")
        sequence = sequence.replace(' ', "")
        pattern = pattern.replace(' ', "")
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        sequence = ''
        pattern = input("Enter pattern, P, that you want to find matches in string: \n")
        pattern = pattern.replace(' ',"")     # strip out any whitespace
        with open(filename, 'r') as f:        # if passing a file, read file and strip all whitespace and newlines
            for line in f:
                sequence = sequence + line.replace(' ', "")
    else:
        print("Pass no arguments for prompt to enter string and pattern, or pass one argument for file path to file containing sequence.")
    
    sequenceList = list(sequence)   # create list to pass to createZTable
    patternList = list(pattern)     # create list to pass to createZTable
    zValues = createZTable(sequenceList)
    print("Z-values: " + str(zValues))
    matches = exactMatch(patternList, sequenceList)
    numberOfMatches = matches[0]
    longestMatch = matches[1]
    print("Number of matches: " + str(numberOfMatches))
    print("Longest match: " + str(longestMatch))



if __name__ == "__main__":
    main()
