import random

def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Initialize swapped to track if any swaps occur
        swapped = False

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                # Mark that a swap has occurred
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

def linear_search(arr, x):
    print("\nMethod : Linear Search")
    flag = False
    counter = 0
    for i in range(len(arr)):
        counter += 1
        if arr[i] == x:
            flag = True
            print("{} has been found at position = {} during iteration counter = {}".format(x,counter-1,counter))

    if flag==False:
        print("{} is missing in the list.".format(x))

def binary_search(arr, x):
    print("\nMethod : Binary Search")
    flag = False
    counter = 0
    start_point = 0
    end_point = len(arr) - 1

    while start_point <= end_point:
        counter += 1
        midpoint = (start_point + end_point) // 2
        if arr[midpoint] == x:
            flag = True
            print("{} has been found at position = {} during iteration counter = {}".format(x, counter - 1, counter))
            break
        elif arr[midpoint] < x:
            start_point = midpoint + 1
        else:
            end_point = midpoint - 1

    if flag==False:
        print("{} is missing in the list.".format(x))

arr = list(set([random.randint(1,100) for i in range(1000)]))
bubble_sort(arr)

search_val = int(input("Enter the value you want to search for: "))
linear_search(arr, search_val)
binary_search(arr, search_val)


