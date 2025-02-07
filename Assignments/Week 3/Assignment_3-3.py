numbers = input().split(" ")
n = len(numbers)
numbers = [int(numbers[i]) for i in range(n)]

answer = []

for i in range(n):
  if (i%2 == 0):
    answer.append(numbers[i]+numbers[-i-1])
  else :
    answer.append(numbers[i])
  
print(' '.join(map(str,answer)), end='')