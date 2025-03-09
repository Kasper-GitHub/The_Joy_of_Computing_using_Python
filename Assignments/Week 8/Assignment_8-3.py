input_tuple = eval(input())
n = len(input_tuple)
prod_lst = []

for i in range(1,n):
    prod = input_tuple[i]*input_tuple[i-1]
    prod_lst.append(prod)

output_tuple = tuple(prod_lst)
print(output_tuple,end='')