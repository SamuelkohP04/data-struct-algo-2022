# Bubble Sort
def bubbleSort(array):

    # loop through each element in the array
    for i in range(len(array)):

        # loop to compare elements in unsorted part of array
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements and swap them if the element on the left is greater than the element on the right
            if array[j] > array[j + 1]:

                # swap positions of elements
                array[j], array[j + 1] = array[j + 1], array[j]


data = [-1, -50, 10, 500, 4, 8, 9, 1, 0]

bubbleSort(data)
print(data)

# Bubble Sort Optimized Version
def optimizedBubbleSort(array):

    # loop through each element in the array
    for i in range(len(array)):

        # keep track of whether swapping is performed in the particular iterations
        swapped = False

        # loop to compare elements in unsorted part of array
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements and swap them if the element on the left is greater than the element on the right
            if array[j] > array[j + 1]:

                # swap positions of elements
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        # if no swap performed in this iteration, it implies that the array has been sorted
        # thus, break loop to remove the need to continue executing the remaining iterations, and reduces execution time
        if not swapped:
            break


data = [-1, -50, 10, 500, 4, 8, 9, 1, 0]

optimizedBubbleSort(data)
print(data)
