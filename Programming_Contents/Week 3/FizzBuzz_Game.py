n = int(input("Enter the starting point : "))

for i in range(n,n+50):
    if i % 5 == 0 and i % 3 == 0:
        print(i,"\tFizzBuzz")
    elif i % 3 == 0:
        print(i,"\tFizz")
    elif i % 5 == 0:
        print(i,"\tBuzz")
    else :
        print(i)