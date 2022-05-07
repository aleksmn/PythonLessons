# Банкомат допускает использование 4-значных pin-кодов.
# Pin-код может содержать только цифры.
# Если мы вводим правильный pin-код, то программа выводит 1,
# иначе — 0.


# pin = '1234'

# if pin.isnumeric() and len(pin) == 4:
#     print(1)


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

string = "доход"

reversed = ""


for i in string:
    reversed = i + reversed


if (reversed == string):
    print(1)
else:
    print(0)


# Cпособ 3

# a = 'доход'


# if(a[::-1] == a):
#     print(1)
# else:
#     print(0)
