import random

number = random.randint(0, 5)

print("Попробуй угадать число от 0 до 5!")

# Попытки
attempts = 3
user_number = None

while attempts > 0 and user_number != number:
    # Спрашиваем у пользователя (В ЦИКЛЕ)
    user_number = int(input("Введи число: "))

    if number == user_number:
        print("Это верно, я загадал число", number)
    else:
        print("Не угадал")

    attempts = attempts - 1


# Вывод результата (ПОСЛЕ ЦИКЛА)

if user_number == number:
    print("Ты выиграл!")
    
else:
    print("Ты проиграл!")
