numbers = input().split(" ")
n = len(numbers)
sum_numbers = 0

for i in range(n):
  sum_numbers += int(numbers[i])

average = round(sum_numbers/n)

print(average, end="")