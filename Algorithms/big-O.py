# О большое


# Константная временная сложность
# O(1)

# def getFirst(myList):
#     return myList[0]

# print(getFirst([9, 5, 6]))

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


# def searchBinary(myList, item):
#     first = 0
#     last = len(myList) - 1
#     isFound = False

#     while (first <= last and not isFound):
#         # Индекс центрального элемента
#         mid = (first + last) // 2
#         if myList[mid] == item:
#             isFound = True
#         else:
#             if item < myList[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1

#     return isFound



# a = [3, 8, 15, 22, 31, 40, 18]

# print(searchBinary(a, 15))


# ========================================

# Временная сложность основных типов (структур) данных

# Список
#    0  1  2  3  4
# a = [1, 2, 3, 4, 5]

# # Удаление: временная сложность O(n)
# del a[0]
# print(a)
# #  0  1  2  3
# # [2, 3, 4, 5]


# # Добавление O(1)
# a.append(9)
# print(a)

# # Срез: O(n)
# b = a[1:4]

# # Извлечение: O(n)
# print(a.pop(0))


# Кортеж
# неизменяемый тип данных
# Добавление O(1)

# t = (1, 2, 3)
# my_list = list(t)
# print(my_list)
# my_tuple = tuple(my_list)
# print(my_tuple)


# Словарь
# Добавление по ключу и удаление по ключу - O(1)
# d = {
#     1: 324,
#     2: 3245,
#     3: 3245
# }

# del d[1]
# print(d)



# Множество:  O(1)
# my_set = {2, 4, 5}

# my_set.add(9)
# my_set.add(2)

# print(my_set)











