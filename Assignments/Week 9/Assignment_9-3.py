def hillvalley(l):
    if len(l) < 3:  # A hill or valley needs at least 3 elements
        return False

    # Find the "peak" or "trough" — the point where the sequence switches direction
    i = 1
    # Ascending part
    while i < len(l) and l[i] > l[i - 1]:
        i += 1

    # If there's no ascending part or it's too short, it's not a hill/valley
    if i == 1 or i == len(l):
        return False

    # Descending part
    while i < len(l) and l[i] < l[i - 1]:
        i += 1

    # If we reached the end, it's a hill
    if i == len(l):
        return True

    # Now check for valley — descending followed by ascending
    i = 1
    while i < len(l) and l[i] < l[i - 1]:
        i += 1

    if i == 1 or i == len(l):
        return False

    while i < len(l) and l[i] > l[i - 1]:
        i += 1

    return i == len(l)


data = eval(input())
print(hillvalley(data), end='')