print("* Программа обработки данных *")


data = input("Введите список чисел через пробел: ")


print(data)

# Получаем список из строки
arr = data.split(" ")

nums = []

for n in arr:
    try:
        nums.append(int(n))
    except:
        pass


print(nums)

# Короткая запись:
# nums = [int(n) for n in arr]
