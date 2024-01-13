# Множества 
# Set
# Операции со множествами

prog = {'CSS', 'Python', 'HTML', 'C++', 'Go'}

lang = {'Python', 'Java','Go', 'CSS', 'Rust'}

'''

1. Создать множество, которое включает значения из первого и второго множества.
2. Вывести только элементы, которые встречаются в обоих множествах.
3. Удалить из первого множества все элементы, которые есть во втором множестве.
4. Вывести из двух множеств элементы, которые встречаются в одном, но не встречаются в другом множестве.


'''


# Объединение
print("union:")
print(prog.union(lang))
print(prog | lang)


# Пересечение
print('intersection')
print(prog.intersection(lang))
print(prog & lang)


# Разность
print('difference')
print(lang.difference(prog))
print(lang - prog)


# Симметричная разность
print('symmetric difference',)
print(prog.symmetric_difference(lang))
print(prog ^ lang)












# print("Union минус Intersection")
# print( (prog | lang) - (prog & lang) )



# # Update
# print(prog)
# prog.update(lang)
# print(prog)







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
