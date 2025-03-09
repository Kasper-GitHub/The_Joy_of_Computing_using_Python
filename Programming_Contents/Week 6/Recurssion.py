'''
Fibonacci sequence:
0th fib no = 0
1st fib no = 1

2nd fib no = 1
3rd fib no = 2
4th fib no = 3
5th fib no = 5
'''

# To find the nth Fibonacci number
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Enter a non-negative number :\t'))

if n < 0:
    print('Fibonacci numbers are undefined for negative numbers')
else:
    print('Fibonacci number at position ', n, ' is ', fibonacci(n))