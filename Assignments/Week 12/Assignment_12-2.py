def frequencySort(s):
    n = len(s)
    j = 0
    frequency = []
    while j < n:
        frequency.append(s.count(s[j]))
        j += 1

    distribution = dict(zip(s, frequency))

    sorted_distribution = dict(sorted(distribution.items(), key=lambda item: (-item[1], item[0])))

    final_list = [key for (key, value) in sorted_distribution.items()]

    return final_list