def indexOf(myList, value):
    for i in range(len(myList)):
        if myList[i] == value:
            return i
    return -1

myList = [1, 2, 3, 4, 5, 6, 7, 9]

print(indexOf(myList, 3))