import random
number = random.randint(0, 5)
print("Попробуй угадать число от 0 до 5!")

# Количество попыток
attempts = 3

while attempts > 0:
    user_number = int(input("Введи число:\n"))
    attempts -= 1

    if user_number == number:
        print("Число угадано! Молодец!")
        # выход из цикла
        break
    elif attempts == 0:
        print("Ты проиграл!")

    else:
        print("Не угадал!")