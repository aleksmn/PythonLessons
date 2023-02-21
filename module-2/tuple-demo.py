# Кортеж (tuple)

my_tuple = (1, 2.5, 'hello')

print(type(my_tuple))

print(my_tuple[1])

print(my_tuple[0:2])

# Tuple является неизменяемой упорядоченной коллекцией 
# my_tuple[0] = 9


# Можно, как и список, перебирать с помощью цикла

for item in my_tuple:
    print(item)

# Преобразуем кортеж в список

my_list = list(my_tuple)

print(my_list)