
a = input("Введите строку: ")

b = a.count(" ")

print("Кол-во слов: ", b+1)
print("Кол-во символов: ", len(a))

# Сколько символов без пробелов

c = a.replace(' ', '')
print("Кол-во символов без пробелов:", len(c))




# Дана строка a, состоящая из цифр.
# Замени все цифры, которые больше 4, на 1, остальные на 0.

s = "9415672"
res = s.replace("1", "0").replace("2", "0").replace("3", "0").replace("4", "0")

res = res.replace("5", "1").replace("6", "1").replace(
    "7", "1").replace("8", "1").replace("9", "1")

print("Исходная строка:", s)
print("Новая строка:", res)


# Посчитай количество слов ( «—» не является словом).
# a = 'int - это целочисленный тип данных'

# print(a.replace(' -', ''))
# print('Количество слов:', a.replace(' -', '').count(' ')+1)

# print('-'*10)

# Даны 3 строки a, b, c — фамилия, имя и отчество соответственно.
# Составь строку из инициалов данного ФИО.

# a, b, c = "Иванов", "Степан", "Александрович"

# print(a, b, c)
# print(a[0] + '.' + b[0] + '.' + c[0])
# print(f'{a[0]}.{b[0]}.{c[0]}')

# Дана строка a. Удали все пробелы из данной строки.

# s = "Я программирую на Python"

# result = s.replace(' ', '')
# print(result)


# Дана строка a, состоящая из цифр. Замени все цифры, которые больше 4, на 1, остальные на 0.

# s = "9415672"

# result = s.replace('5', '1').replace(
#     '6', '1').replace('7', '1').replace('8', '1').replace('9', '1')


# result = result.replace('4', '0').replace(
#     '3', '0').replace('2', '0')
# print(result)


# Используя циклы:

# string = "9415672"
# new_string = ""
# for x in string:
#     if int(x) > 4:
#         new_string = new_string + '1'
#     else:
#         new_string = new_string + '0'
# print(new_string)


# # Дана строка a. Посчитай количество цифр в данной строке.

# s = "Пр20ив11е5т"

# result = s.count('0') + s.count('1') + s.count('2') + \
#     s.count('3') + s.count('4') + s.count('5') + \
#     s.count('6') + s.count('7') + s.count('8') + s.count('9')


# print(result)

# string = "Пр20ив11е5т"
# num_count = 0

# for x in string:
#     if x.isdigit():
#         num_count += 1

# print(num_count)
