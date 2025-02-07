numbers = input().split(" ")
n = len(numbers)
numbers = [int(numbers[i]) for i in range(n)]

unique = [numbers[0]]

for i in range(1,n):
  if (numbers[i] % 2 != 0):
    unique.append(numbers[i])
  elif (unique.count(numbers[i]) == 0):
    unique.append(numbers[i])

print(' '.join(map(str,unique)), end='')