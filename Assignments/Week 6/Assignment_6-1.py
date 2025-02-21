def find_kth_smallest(arr, k):
    if k > len(arr):
        return "The clue k should be smaller than or equal to the list size"

    arr.sort()  # Sorting the array in ascending order
    return arr[k - 1]  # Returning the k-th smallest element


# Taking input from the user
arr = list(map(int, input().split()))
k = int(input())

# Printing the result
print(find_kth_smallest(arr, k),end='')







# def bubble_sort(arr):
#     # Outer loop to iterate through the list n times
#     for n in range(len(arr) - 1, 0, -1):
#
#         # Initialize swapped to track if any swaps occur
#         swapped = False
#
#         # Inner loop to compare adjacent elements
#         for i in range(n):
#             if arr[i] > arr[i + 1]:
#                 # Swap elements if they are in the wrong order
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
#                 # Mark that a swap has occurred
#                 swapped = True
#
#         # If no swaps occurred, the list is already sorted
#         if not swapped:
#             return arr
#
#
# numbers = []
# numbers_lst = input().split()
#
# for i in numbers_lst:
#     if i.isnumeric() == True:
#       numbers.append(int(i))
#
# n = len(numbers)
# #numbers = [int(numbers[i]) for i in range(n)]
# numbers_sorted = bubble_sort(numbers)
#
# magic_clue = int(input())
#
# if magic_clue > n:
#   print("The clue k should be smaller than or equal to the list size",end='')
# else:
#   print(numbers_sorted[magic_clue-1],end='')