# Merge Sort
def mergeSort(array):
    # sorting would not be needed if there is only one element
    if len(array) > 1:

        # middle index of array
        # // has the same effect as math.floor(). The purpose is to round down the result to the nearest integer
        mid = len(array) // 2

        # left half of the array
        left = array[:mid]
        # right half of the array
        right = array[mid:]

        # sort both half of the array
        mergeSort(left)
        mergeSort(right)

        # i would be use to iterate through the left half of the array
        # j would be use to iterate through the right half of the array
        # k would be use to iterate through the original array to replace elements with the sorted elements
        i = j = k = 0

        # while both half of arrays contain elements
        while i < len(left) and j < len(right):
            # if the current element in the left array is less than the current element in the right array,
            # replace the first element in the unsorted part of the original array (array[k]) with the current element in the left array left[i]
            # else replace the first element in the unsorted part of the original array (array[k]) with the current element in the right array right[j]
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # after the previous while loop, elements in one half of the original array has all been used
        # thus, we would now replace the elements in unsorted part of array, with the remaining elements in the other half of the array

        # if there are remaining elements in the left half of the array
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # if there are remaining elements in the right half of the array
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


data = [-1, -50, 10, 500, 4, 8, 9, 1, 0]

mergeSort(data)
print(data)
