def remove_strings_from_tuples(lst):
    # Iterate through the list and filter out strings from each tuple
    return [tuple(item for item in tup if not isinstance(item, str)) for tup in lst]

# Example input
input_list = eval(input())

# Process the input list
output_list = remove_strings_from_tuples(input_list)

# Display the result
print(output_list,end='')