numbers = input().split(" ")
n = len(numbers)
numbers = [int(numbers[i]) for i in range(n)]
numbers.sort()

j=1
while (numbers[j] == numbers[j-1]):
  j=j+1

print(numbers[j], end="")  