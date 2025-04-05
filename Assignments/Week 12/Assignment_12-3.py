def subsequence(l1, l2):
    i = 0  # pointer for l1
    j = 0  # pointer for l2

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            i += 1  # move to next element in l1
        j += 1  # always move in l2

    return i == len(l1)
