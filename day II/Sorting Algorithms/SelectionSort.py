# Selection Sort
def selectionSort(array):

    size = len(array)

    for i in range(size):
        # set minimum index to the first element of unsorted part of array
        min_index = i

        # iterate through all elements in unsorted part of array to find index of the minimum value
        for j in range(i + 1, size):

            if array[j] < array[min_index]:
                min_index = j

        # swap the first element in unsorted part of array with the minimum value in unsorted part of array
        array[i], array[min_index] = array[min_index], array[i]


data = [-1, -50, 10, 500, 4, 8, 9, 1, 0]

selectionSort(data)
print(data)
