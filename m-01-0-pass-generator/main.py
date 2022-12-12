
import random
import string


print('Добро пожаловать в генератор паролей!')

# print(string.digits)
# print(string.ascii_letters)
# print(string.punctuation)

symbols = string.ascii_letters + string.digits + string.punctuation


number = int(input('Количество паролей?  '))

length = int(input('Количество символов?  '))



for p in range(number):
    password = ''
    for i in range(length):

        password += random.choice(symbols)

    print(password)
