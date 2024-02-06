
a = input("Введите строку: ")

print("Длина строки:", len(a))
print("Количество пробелов:", a.count(" "))
print("Строка без пробелов:", a.replace(" ", "*"))
print("В строке есть слово Python?", "Python" in a)
# нижний регистр
print(a.lower())
# верхний регистр
print(a.upper())