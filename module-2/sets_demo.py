# Множества 
# Set

prog = {'CSS', 'Python', 'HTML', 'C++', 'Go'}

lang = {'Python', 'Java','Go', 'CSS', 'Rust'}

# Добавление
prog.add('C#')
print('SET prog:', prog)

# Удаление
lang.remove('Go')
print('SET lang:', lang)

'''

1. Создать множество, которое включает значения из первого и второго множества.
2. Вывести только элементы, которые встречаются в обоих множествах.
3. Удалить из первого множества все элементы, которые есть во втором множестве.
4. Вывести из двух множеств элементы, которые встречаются в одном, но не встречаются в другом множестве.


'''


# Union (объединение)

print('Union:', prog.union(lang))
print('Union:', prog | lang)


# Intersection (пересечение)

print("Intersection", prog.intersection(lang))
print("Intersection", prog & lang)


# Difference (разность)

print('Difference:', lang.difference(prog))
print('Difference:', lang - prog)


# Symmetric difference (Симметричная разность)

print('Symmetric difference:', prog.symmetric_difference(lang))
print('Symmetric difference:', prog ^ lang)


print("Union минус Intersection")
print( (prog | lang) - (prog & lang) )



# Update
print(prog)
prog.update(lang)
print(prog)







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
