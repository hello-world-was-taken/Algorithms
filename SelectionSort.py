def swap(arr, index_one, index_two):
    '''A simple swapping function that takes an array(list) and indexes to swap'''
    temp = arr[index_one]
    arr[index_one] = arr[index_two]
    arr[index_two] = temp

def selectionSort(arr):
    '''An implementation of selection sort'''
    for i in range(len(arr)):
        minIndex = i # the value that keeps track of the current minimum index
        for j in range(i + 1, len(arr)): # start comparing from the i'th value to the end of the loop with our swapping but updating the minimum index
            if(arr[minIndex] > arr[j]):
                minIndex = j
        swap(arr, i, minIndex) # finally swap the minimum index with the current i'th index


# arr = [5, 3, 4, 1, 2]
arr = [0, 2, 34, 22, 10, 19, 17]

selectionSort(arr)

print(arr)