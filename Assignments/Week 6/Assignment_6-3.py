import sys

def delete_elements(lst, item):
    if not lst:  # Base case: if list is empty, return empty list
        return []

    # Recursive case: exclude the item if it matches, otherwise include it
    if lst[0] == item:
        return delete_elements(lst[1:], item)
    else:
        return [lst[0]] + delete_elements(lst[1:], item)


# Reading input correctly from standard input
data = sys.stdin.read().strip().split("\n")  # Read all input lines
lst = list(map(int, data[0].split()))  # First line is the list
item = int(data[1])  # Second line is the item to remove

# Computing the result
result = delete_elements(lst, item)

# Printing the result correctly in required format
print(" ".join(map(str, result)), end="")