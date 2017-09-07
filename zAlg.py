def zAlg(s):

    # This builds the z string
    Z = [0] * len(s)
    Z[0] = len(s)

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


t = ['x', 'a', 'a', 'a', 'x', 'a', 'a', 'y']
testRun = zAlg(t)
print(testRun)
