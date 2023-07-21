# Множества 
# Set

prog = {'CSS', 'Python', 'HTML', 'C++', 'Go'}

lang = {'Python', 'Java','Go', 'CSS', 'Rust'}

prog.add('C#')
print('SET prog:', prog)

lang.remove('Go')
print('SET lang:', lang)
'''

1. Создать множество, которое включает значения из первого и второго множества.
2. Вывести только элементы, которые встречаются в обоих множествах.
3. Удалить из первого множества все элементы, которые есть во втором множестве.
4. Вывести из двух множеств элементы, которые встречаются в одном, но не встречаются в другом множестве.


'''








# Union (объединение)
my_stack_1 = prog.union(lang)
my_stack_2 = prog | lang

print('Union:', my_stack_1)
print('Union:', my_stack_2)


# # Intersection (пересечение)
my_stack_1 = prog.intersection(lang)
my_stack_2 = prog & lang

print('Intersection:', my_stack_1)
print('Intersection:', my_stack_2)


# # Difference (разность)
my_stack_1 = lang.difference(prog)
my_stack_2 = lang - prog

print('Difference:', my_stack_1)
print('Difference:', my_stack_2)



# # Symmetric difference (Симметричная разность)
my_stack_1 = prog.symmetric_difference(lang)
my_stack_2 = prog ^ lang

print('Symmetric difference:', my_stack_1)
print('Symmetric difference:', my_stack_2)




# # Update
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
