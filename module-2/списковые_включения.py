# Списковые включения
# list comprehensions

numbers = [num**2 for num in range(1, 101)]
print(numbers)


fruits = ['apple', 'banana', 'cherry']
# найдем длину каждого слова и создадим список из этих длин
# [5, 6, 6]
lens = [len(x) for x in fruits]
print(lens)