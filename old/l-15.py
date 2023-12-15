
#Список товаров

n = int(input("Сколько товаров? "))

arr = []

for x in range(n):
    arr.append([input("Товар: "), input("Вес: ")])


print(arr)

for t in arr:
    print(t)







# Дано целое положительное число A. 
# Следует создать и вывести список размера A, 
# содержащий A первых положительных нечётных чисел.


# print("Находим N первых положительных чисел")
# n = int(input("Введите число: "))

# arr = []
# i = 1

# for x in range(n):
#     arr.append(i)
#     i = i + 2

# print(arr)
