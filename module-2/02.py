# Сортировка пузырьком

numbers = input('Список чисел: ').split()

# numbers = list(map(int, numbers))

numbers = [int(n) for n in numbers]

# print(numbers)

for num in range(len(numbers)):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)
