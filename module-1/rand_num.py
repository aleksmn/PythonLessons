import random
number = random.randint(0, 100)
print("Попробуй угадать число от 0 до 100!")

# Количество попыток
attempts = 7

while attempts > 0:
    user_number = int(input("Введи число:\n"))
    attempts -= 1
    if user_number == number:
        break
    elif user_number < number:
        print("Загадано число больше")
    else:
        print("Загадано число меньше")


if user_number == number:
    print("Это верно, я загадал число", number)
else:
    print("Ты проиграл")