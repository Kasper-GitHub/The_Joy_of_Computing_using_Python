def longestCommonPrefix(strng):
    index_counter = 0
    status_chk = 0
    n = len(strng)
    word_len = [len(strng[i]) for i in range(n)]

    for i in range(min(word_len)):
        for j in range(n):
            if strng[j][i] == strng[j-1][i]:
                status_chk += 1
        if status_chk == n:
            index_counter += 1
        status_chk = 0
    return strng[0][:index_counter]

strng = eval(input())
print(longestCommonPrefix(strng), end='')