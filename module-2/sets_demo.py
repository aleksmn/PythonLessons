# Операции со множествами

set_1 = {'CSS', 'Python', 'HTML', 'C++', 'Go'}

set_2 = {'Python', 'Java','Go', 'CSS', 'Rust'}


'''
1. Создать множество, которое включает значения из первого и второго множества.
2. Вывести только элементы, которые встречаются в обоих множествах.
3. Удалить из первого множества все элементы, которые есть во втором множестве.
4. Вывести из двух множеств элементы, которые встречаются в одном, но не встречаются в другом множестве.

'''


# Объединение
print("union:")
print(set_1.union(set_2))
print(set_1 | set_2)


# Пересечение
print('intersection')
print(set_1.intersection(set_2))
print(set_1 & set_2)


# Разность
print('difference')
print(set_1.difference(set_2))
print(set_1 - set_2)


# Симметричная разность
print('symmetric difference')
print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)


# Объединение минус пересечение
print( (set_1 | set_2) - (set_1 & set_2) )


















# print("Union минус Intersection")
# print( (set_1 | set_2) - (set_1 & set_2) )



# # Update
print(set_1)
set_1.update(set_2)
print(set_1)

# Добавление
set_1.add("JavaScript")

# Удаление
set_1.remove("Rust")














# # Is Subset

# x = {"a", "b", "c"}
# y = {'f', "a", "c", "d", "e", "b"}
# print('Первое множество является подмножеством второго?')
# print(x.issubset(y)) 



# # Is Superset

# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# print('Второе множество является подмножеством первого?')
# print(x.issuperset(y))
