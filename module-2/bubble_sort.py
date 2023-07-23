import random

numbers = input("Введите числа через пробел: ")

numbers = numbers.split()
a = []
for n in numbers:
    a.append(int(n))
numbers = a

for k in range(len(numbers)-1):
    # Один проход сортировки
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


# Вывод результата
print('Сортировка пузырьком:', numbers)







# TEST RANDOM LIST
# Создаем случайный список из 1000 значений

# numbers = []

# for i in range(50000):
#     numbers.append(random.randint(0, 10000000))


# print('sorted', sorted(numbers))


