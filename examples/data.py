print("* Программа обработки данных *")

data = input("Введите список чисел через пробел: ")

# print(data)

# Получаем список из строки
arr = data.split(" ")

nums = []

for n in arr:
    try:
        nums.append(int(n))
    except:
        pass

# Короткая запись:
# nums = [int(n) for n in arr]

print(nums)


smallest = None

for x in nums:
    if smallest is None or x < smallest:
        smallest = x
    # print(x, smallest)
    
print("Минимум:", smallest)


biggest = None

for x in nums:
    if biggest is None or x > biggest:
        biggest = x
    # print(x, biggest)

print("Максимум:", biggest)
