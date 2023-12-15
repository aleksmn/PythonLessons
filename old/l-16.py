print("\n* Находим минимальное значение из списка *\n")


string = input("Введите числа через пробел: ")

# Получаем список из строки
arr = string.split(" ")

nums = []

for n in arr:
    nums.append(int(n))


# Короткая запись:
# nums = [int(n) for n in arr]


print(nums)

smallest = 0

for x in nums:
    if x < smallest:
        smallest = x
    print(x, smallest)
print("Минимум:", smallest)






# smallest = None

# for x in nums:
#     if smallest is None or x < smallest:
#         smallest = x
#     print(x, smallest)
# print("Минимум:", smallest)
