word_chunk = input().split(" ")
n = len(word_chunk)
word_chunk = [word_chunk[i].lower() for i in range(n)]

j = 0
frequency = []

while j < n:
    frequency.append(word_chunk.count(word_chunk[j]))
    j += 1

distribution = dict(zip(word_chunk, frequency))

for key, value in distribution.items():
    print(f"{key}: {value}")