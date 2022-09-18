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

        # after the previous while loop, there might still be remaining elements in one half of the array
        # thus, we will be replacing the elements in the unsorted part of the orignal array with these remaining elements

        # while there are remaining elements in the left half of the array, replace the elements in the unsorted part of the orignal array with these remaining elements
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # while there are remaining elements in the right half of the array, replace the elements in the unsorted part of the orignal array with these remaining elements
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


data = [-1, -50, 10, 500, 4, 8, 9, 1, 0]

mergeSort(data)
print(data)
