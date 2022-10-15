



names = []

name = ''

while name != 'q':
    name = input("Введите имя (q - выйти): ")
    if name != "q":
        names.append(name)


print(names)