n = int(input("Enter the number for multiplication table : "))

print("The multiplication table of ",n," is:")
for i in range(1,11):
    print(n,"\tx\t",i,"\t=\t",n*i)