def binarySearch(myList, value):
    mini = 0
    maxi = len(myList) - 1
    mid = (mini + maxi) // 2

    while(myList[mid] != value and mini <= maxi):
        if(myList[mid] > value):
            maxi = mid - 1
        elif(myList[mid] < value):
            mini = mid + 1
        print("inside the loop")
        mid = (mini + maxi) // 2

    if(myList[mid] == value):
        return mid
    else: 
        return - 1

myList = [1, 2, 3, 4, 5, 6, 7, 9]

print(binarySearch(myList, -19))