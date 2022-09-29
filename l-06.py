# Банкомат допускает использование 4-значных pin-кодов.
# Pin-код может содержать только цифры.
# Если мы вводим правильный pin-код, то программа выводит 1,
# иначе — 0.


# pin = '1234'

# if pin.isnumeric() and len(pin) == 4:
#     print(1)


# pin = input("Введите PIN  ")

# if pin.isnumeric() == False:
#     print("NOT OK")

# else:
#     pin = int(pin)
#     if pin > 999 and pin <= 9999:
#         print("OK")

#     else:
#         print("NOT OK")


# Дана строка a. Если данная строка является палиндромом, то выведи 1, иначе — 0.


# Cпособ 1
# string = "доход"

# reversed = ""


# for i in range(1, len(string)+1):
#     reversed += string[-i]

# if (reversed == string):
#     print(1)
# else:
#     print(0)


# Cпособ 2

# string = "доход"

# reversed = ""


# for i in string:
#     reversed = i + reversed


# if (reversed == string):
#     print(1)
# else:
#     print(0)


# Cпособ 3

# a = 'доход'


# if(a[::-1] == a):
#     print(1)
# else:
#     print(0)


# Программа получает на вход целое число a. Если это число является
# целочисленным полным квадратом, тогда выведи следующий целочисленный
# полный квадрат, иначе выведи −1.


a = 4

# print(a ** (1/2))
# print(2.0 % 1 == 0)
# print(2.1 % 1 == 0)


if (a ** (1/2)) % 1 == 0:
    print('1')
    print(a ** (1/2) + 1)

else:
    print("-1")
