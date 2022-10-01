print("* Программа обработки данных *")


data = input("Введите список чисел через пробел: ")


print(data)

# Получаем список из строки
arr = data.split(" ")

nums = []

for n in arr:
    if n.isnumeric():
     nums.append(int(n))


print(nums)

# Короткая запись:
# nums = [int(n) for n in arr]
