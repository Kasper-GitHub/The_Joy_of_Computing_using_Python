word_chunk = input().split(" ")
n = len(word_chunk)
final_list = [word_chunk[0]]

def sortString(str):
    return ''.join(sorted(str))

for i in range(1,n):
    for j in range(i):
        if len(word_chunk[i]) == len(word_chunk[j]):
            if sortString(word_chunk[i]) != sortString(word_chunk[j]):
                if not any(sortString(x) == sortString(word_chunk[i]) for x in final_list):
                    final_list.append(word_chunk[i])
        else:
            if not any(sortString(x) == sortString(word_chunk[i]) for x in final_list):
                final_list.append(word_chunk[i])

print(' '.join(sorted(final_list)),end='')
