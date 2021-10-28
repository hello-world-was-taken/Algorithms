def swap(arr, index_one, index_two):
    temp = arr[index_one]
    arr[index_one] = arr[index_two]
    arr[index_two] = temp

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if(arr[i] > arr[j]):
                swap(arr, i, j)

arr = [100, 3, 99, 5, 1, 7, 34, 86, 6, 78, 43, 34, 54, 23, 12, 11, 10]

bubbleSort(arr)

print(arr)