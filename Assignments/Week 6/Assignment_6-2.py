def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

# Taking input from the user
n = int(input())

# Handling edge case when input is 0
if n == 0:
    print("0",end='')
else:
    print(decimal_to_binary(n),end='')