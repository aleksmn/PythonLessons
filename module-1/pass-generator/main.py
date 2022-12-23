
import random
import string

print('Добро пожаловать в генератор паролей!')

symbols = string.ascii_letters + string.digits + "@$#()[]!?&/|*%-=+"


number = int(input('Количество паролей?  '))

length = int(input('Количество символов?  '))


for p in range(number):
    
    # Создаем пароль
    password = ''
    for i in range(length):
        password += random.choice(symbols)

    print(password)
