print("\n* Программа обработки данных *\n")

data = input("Введите список чисел через пробел: ")

# print(data)

# Получаем список из строки
a = data.split()

nums = []

for n in a:
    try:
        nums.append(float(n))
    except:
        pass


print(nums)











# summa = 0

# for n in nums:
#     summa = summa + n

# print("Сумма: ")
# print(summa)

# print("Среднее арифметическое: ")
# print(summa / len(nums))



# # Короткая запись:
# # nums = [int(n) for n in arr]

# print(nums)


# smallest = None

# for x in nums:
#     if smallest is None or x < smallest:
#         smallest = x
#     # print(x, smallest)
    
# print("Минимум:", smallest)


# biggest = None

# for x in nums:
#     if biggest is None or x > biggest:
#         biggest = x
#     # print(x, biggest)

# print("Максимум:", biggest)



# Функции


# def getCount(arr):
#     count = 0
#     for x in arr:
#         count = count + 1
#     return count


# def getSum(arr):
#     sum = 0
#     for x in arr:
#         try:
#             x = int(x)
#         except:
#             x = 1
#         sum = sum + x
#     return sum


# def minNumber(arr):
#     smallest = None
#     arr = [int(x) for x in arr]
#     print(arr)
#     for i in arr:
#         if smallest is None or i < smallest:
#             smallest = i
#         #print(i, smallest)
#     print("Минимум:", smallest)


# inputArr = input("Введите числа через пробел: ").split(" ")

# minNumber(inputArr)
