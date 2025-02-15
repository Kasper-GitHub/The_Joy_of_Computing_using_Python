word_chunk = input().split(" ")
n = len(word_chunk)
word_chunk = [word_chunk[i].lower() for i in range(n)]

j = 0
frequency = []

while j < n:
    frequency.append(word_chunk.count(word_chunk[j]))
    j += 1

distribution = dict(zip(word_chunk, frequency))

store = list(distribution.items())

for i in range(len(store)-1):
    key = store[i][0]
    value = store[i][1]
    print(f"{key}: {value}")

key = store[len(store)-1][0]
value = store[len(store)-1][1]
print(f"{key}: {value}", end="")