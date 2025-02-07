numbers = input().split(" ")
n = len(numbers)
numbers = [int(numbers[i]) for i in range(n)]
numbers.sort()

j = 0
frequency =  []
while j < n : 
    frequency.append(numbers.count(numbers[j])) 
    j += 1

distribution = dict(zip(numbers, frequency)) 
    
mode = [key for (key,value) in distribution.items() if value == max(frequency)]

print(mode[0], end="")