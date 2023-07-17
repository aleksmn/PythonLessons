# О большое


# Константная временная сложность
# O(1)

def getFirst(myList):
    return myList[0]

print(getFirst([9, 5, 6]))

# Время выполнения не зависит от размера массива



# Линейная временная сложность
# O(n)
# время выполнения прямо пропорционально размеры входных данных

# функция нахождения суммы массивы

# def getSum(myList):
#     sum = 0

#     for i in myList:
#         sum += i

#     return sum

# print(getSum([5, 8, 12]))



# Квадратичная временная сложность 
# O(n^2)

# myList = [[1, 4], [5, 6], [9, 5], [14, 3]]

# def getSum2(myList):
#     sum = 0
#     for row in myList:
#         for item in row:
#             sum += item
#     return sum

# print(getSum2)



# Логарифмическая временная сложность 
# O(log n)


def searchBinary(myList, item):
    first = 0
    last = len(myList) - 1
    isFound = False

    while (first <= last and not isFound):
        # Индекс центрального элемента
        mid = (first + last) // 2
        if myList[mid] == item:
            isFound = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return isFound



a = [3, 8, 15, 22, 31, 40, 18]

print(searchBinary(a, 15))



